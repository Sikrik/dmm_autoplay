import cv2
import pyautogui
from time import sleep
from paddleocr import PaddleOCR
import gc  # 导入垃圾回收模块

#预定class化

# 初始化全局变量
ocr = None
current_lang = None
last_screenshot_path = "./pic/screenshotOCR.png"



# 初始化 OCR 模型
def init_ocr(lang='ch'):
    global ocr, current_lang
    if ocr is None or lang != current_lang:
        ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False)
        current_lang = lang


# 截图并进行 OCR 识别
def capture_and_ocr(region=None, reuse_last=False):
    global last_screenshot_path
    screenshot_path = last_screenshot_path
        #if reuse_last and last_screenshot_path else "./pic/screenshot.png"
    if not reuse_last or not last_screenshot_path:
        pyautogui.screenshot(region=region).save(screenshot_path)  # 截图并保存
        last_screenshot_path = screenshot_path  # 缓存路径

    img = cv2.cvtColor(cv2.imread(screenshot_path), cv2.COLOR_BGR2RGB)

    # 进行 OCR 识别
    result = ocr.ocr(img)
    return result if result else []


# 获取文本的坐标
def get_text_position(word, region=None):
    x = (word[0][0][0] + word[0][1][0]) / 2 + (region[0] if region else 0)
    y = (word[0][0][1] + word[0][2][1]) / 2 + (region[1] if region else 0)
    return x, y

#获取数值
def find_value(region = None):
    init_ocr()  # 初始化 OCR
    result = capture_and_ocr(region)

    if not result:
        print(f"未识别到任何文本。")
        return

    print("OCR 结果:", result)  # 输出 OCR 结果用于调试

    # 查找目标数值并返回
    for line in result:
        if line:
            for word in line:
                print(word[1][0])
                return int(word[1][0])

# 识别并点击文本
def find_and_click_text(target_text, region=None, lang='ch', reuse_last_screenshot=False):
    init_ocr(lang)  # 初始化 OCR
    result = capture_and_ocr(region, reuse_last_screenshot)

    if not result:
        print(f"未识别到任何文本。")
        return

    print("OCR 结果:", result)  # 输出 OCR 结果用于调试

    # 查找目标文本并点击
    for line in result:
        if line:
            for word in line:
                if word and target_text in word[1][0]:
                    x, y = get_text_position(word, region)
                    pyautogui.click(x, y, button='left', duration=0.5)
                    print(f"点击文本 '{target_text}' at x={x}, y={y}")
                    sleep(1)
                    return

    print(f"未找到文本 '{target_text}'")


# 检查是否存在目标文本
def check_text(target_text, region=None, lang='ch', reuse_last_screenshot=False):
    init_ocr(lang)  # 初始化 OCR
    result = capture_and_ocr(region, reuse_last_screenshot)

    if not result:
        print(f"未识别到任何文本。")
        return False

    print("OCR 结果:", result)  # 输出 OCR 结果用于调试

    # 查找目标文本
    for line in result:
        if line:
            for word in line:
                if word and target_text in word[1][0]:
                    x, y = get_text_position(word, region)
                    print(f"识别到文本 '{target_text}' at x={x}, y={y}")
                    return True

    print(f"未找到文本 '{target_text}'")
    return False


# 手动释放 OCR 对象
def release_ocr():
    global ocr
    ocr = None
    gc.collect()  # 手动触发垃圾回收
