import os

import cv2
import pyautogui
import logging
from time import sleep
from paddleocr import PaddleOCR
import gc

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OCRClickTool:
    def __init__(self, lang='ch',screenshot_path = None):
        """初始化OCRClickTool实例，设置语言和默认截图路径"""
        self.ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False,det=False)
        self.lang = lang
        self.screenshot_path = screenshot_path
        self.last_screenshot = None
        # 确保目录存在
        os.makedirs(os.path.dirname(self.screenshot_path), exist_ok=True)

    def _init_ocr_model(self, lang='ch'):
        """根据指定语言初始化OCR模型"""
        if lang != self.lang:
            self.ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False)
            self.lang = lang

    def _capture_screenshot(self, region=None):
        """截取屏幕并保存到指定路径，返回截图的绝对路径"""
        self.last_screenshot = pyautogui.screenshot(region=region)
        # print(f"{self.screenshot_path}")
        self.last_screenshot.save(self.screenshot_path)
        return self.screenshot_path

    def _ocr_recognition(self, img_path):
        """读取图像并进行OCR识别"""
        try:
            img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
            if img is None:
                logging.error(f"无法读取图像：{img_path}")
                return [None]
            return self.ocr.ocr(img) if self.ocr else []
        except Exception as e:
            logging.error(f"OCR识别过程中发生错误: {e}")
            return [None]

    def find_text_center(self, word, region=None):
        """计算识别文本的中心坐标"""
        if region is None:
            region = (0, 0)
        x_center = (word[0][0][0] + word[0][1][0]) / 2 + region[0]
        y_center = (word[0][0][1] + word[0][2][1]) / 2 + region[1]
        return x_center, y_center

    def find_numeric_value(self, region=None, max_retries=2):
        img_path = self._capture_screenshot(region)
        result = self._ocr_recognition(img_path)
        retries = 0
        while retries < max_retries:
            result = self._ocr_recognition(img_path)
            logging.info(result)
            if result is [None]:
                logging.info("未识别到任何文本，重试中...")
                retries += 1
                sleep(1)  # 等待1秒后重试
                continue
            break  # 识别成功，跳出循环

        logging.info("OCR 识别结果: %s", result)
        for line in result:
            if line is None:
                return None
            for word in line:
                logging.info("识别到的文本: %s", word[1][0])
                return word[1][0]

        logging.info("未识别到数值。")
        return None

    def click_on_text(self, target_text, region=None, lang='ch', reuse_last_screenshot=False, max_retries=2,response_time=2):
        """

        :param target_text: 目标文本
        :param region: 识别的坐标以及识别框
        :param lang: language
        :param reuse_last_screenshot:
        :param max_retries: 最大重试次数
        :return:
        """
        """查找目标文本并在其中心位置点击"""
        self._init_ocr_model(lang)
        img_path = self._capture_screenshot(region)
        retries = 0
        while retries < max_retries:
            result = self._ocr_recognition(img_path)
            logging.info(result)
            if result == [None]:
                logging.info("未识别到任何文本，重试中...")
                retries += 1
                sleep(response_time)  # 等待1秒后重试
                continue

            logging.info("OCR 识别结果: %s", result)
            for line in result:
                for word in line:
                    if target_text in word[1][0]:
                        x, y = self.find_text_center(word, region)
                        pyautogui.moveTo(x, y, duration=0.2)
                        pyautogui.click(button='left')
                        logging.info(f"点击文本 '{target_text}' 位于 x={x}, y={y}")
                        sleep(1)
                        return True
                    # else:
                    #     retries += 1
                    #     return False

            logging.info(f"未找到目标文本 '{target_text}'。")
            retries  += 1
            return False

        logging.error(f"在最大重试次数内未找到目标文本 '{target_text}'。")
        return False


    def check_text_exists(self, target_text, region=None, lang='ch', reuse_last_screenshot=False,response_time=1.5):
        """检查指定文本是否存在于区域内"""
        self._init_ocr_model(lang)
        img_path = self._capture_screenshot(region)
        result = self._ocr_recognition(img_path)

        # 如果 result 是空列表，表示未识别到任何文本，直接返回 False
        if not result:
            logging.info("未识别到任何文本。")
            return False

        logging.info("OCR 识别结果: %s", result)
        for line in result:
            # 确保 line 不是 None
            if line is None:
                continue
            for word in line:
                # 确保 word 不是 None 并且 word[1] 不是 None
                if word is not None and word[1] is not None and target_text in word[1][0]:
                    x, y = self.find_text_center(word, region)
                    logging.info(f"识别到文本 '{target_text}' 位于 x={x}, y={y}")
                    sleep(response_time)
                    return True

        logging.info(f"未找到文本 '{target_text}'。")
        return False

    def release_resources(self):
        """释放OCR资源并手动进行垃圾回收"""
        self.ocr = None
        gc.collect()

# 调用示例
if __name__ == "__main__":
    ocr = OCRClickTool(screenshot_path="../pic/screenshot.png")
    ocr.click_on_text("Project", region=(0,0,400,200), lang='en')