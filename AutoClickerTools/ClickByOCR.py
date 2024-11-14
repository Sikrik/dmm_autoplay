import cv2
import pyautogui
from time import sleep
from paddleocr import PaddleOCR
import gc  # 导入垃圾回收模块
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClickByOCR:
    def __init__(self, lang='ch'):
        # 初始化OCR模型语言和模型实例
        self.ocr = None
        self.current_lang = None
        self.last_screenshot_path = "../pic/screenshotOCR.png"
        self.init_ocr(lang)

    def init_ocr(self, lang='ch'):
        # 初始化 OCR 模型
        if self.ocr is None or lang != self.current_lang:
            self.ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False)
            self.current_lang = lang

    def capture_and_ocr(self, region=None, reuse_last=False):
        # 截图并进行 OCR 识别
        screenshot_path = self.last_screenshot_path
        if not reuse_last or not self.last_screenshot_path:
            # 根据区域进行截图
            pyautogui.screenshot(region=region).save(screenshot_path)
            self.last_screenshot_path = screenshot_path

        # 读取并转换图像格式
        img = cv2.cvtColor(cv2.imread(screenshot_path), cv2.COLOR_BGR2RGB)

        # 进行 OCR 识别
        result = self.ocr.ocr(img)
        if not result:
            logging.info("未识别到任何文本。")
            return []
        logging.info("OCR 结果: %s", result)
        return result

    def get_text_position(self, word, region=None):
        # 获取识别文本的中心坐标
        x = (word[0][0][0] + word[0][1][0]) / 2 + (region[0] if region else 0)
        y = (word[0][0][1] + word[0][2][1]) / 2 + (region[1] if region else 0)
        return x, y

    def find_value(self, region=None):
        # 查找并返回第一个识别到的数值
        self.init_ocr()  # 初始化 OCR
        result = self.capture_and_ocr(region)

        for line in result:
            if line:
                for word in line:
                    if word[1][0].isdigit():  # 检查识别结果是否为数值
                        logging.info("识别到的数值: %s", word[1][0])
                        return int(word[1][0])
        logging.info("未识别到数值。")
        return None

    def find_and_click_text(self, target_text, region=None, lang='ch', reuse_last_screenshot=False):
        # 查找并点击目标文本
        self.init_ocr(lang)
        result = self.capture_and_ocr(region, reuse_last_screenshot)

        for line in result:
            if line:
                for word in line:
                    if word and target_text in word[1][0]:
                        x, y = self.get_text_position(word, region)
                        pyautogui.click(x, y, button='left', duration=0.5)
                        logging.info(f"点击文本 '%s' at x=%d, y=%d", target_text, x, y)
                        sleep(1)
                        return

        logging.info(f"未找到文本 '%s'", target_text)

    def check_text(self, target_text, region=None, lang='ch', reuse_last_screenshot=False):
        # 检查是否存在目标文本
        self.init_ocr(lang)
        result = self.capture_and_ocr(region, reuse_last_screenshot)

        for line in result:
            if line:
                for word in line:
                    if word and target_text in word[1][0]:
                        x, y = self.get_text_position(word, region)
                        logging.info(f"识别到文本 '%s' at x=%d, y=%d", target_text, x, y)
                        return True

        logging.info(f"未找到文本 '%s'", target_text)
        return False

    def release_ocr(self):
        # 手动释放 OCR 对象
        self.ocr = None
        gc.collect()  # 手动触发垃圾回收
        logging.info("OCR 对象已释放")

# 使用示例
# ocr_tool = ClickByOCR(lang='ch')
# ocr_tool.find_and_click_text("目标文本")
# ocr_tool.check_text("检查文本")
# ocr_tool.release_ocr()  # 释放资源