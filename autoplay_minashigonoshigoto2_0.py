import json
from time import sleep
import logging
import pyautogui
from AutoClickerTools2.OCRClickTool import OCRClickTool
from AutoClickerTools2.OpenCVClicker import OpenCVClicker
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login_bonus():
    # 初始化 OCR 以避免多次重复加载
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")

    # 查找并点击目标文本 'dmm'
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500))

    # 查找并点击目标文本 '孤儿的工作'，复用 OCR 实例
    ocr_tool.click_on_text('孤儿的工作', region=(1392, 160, 1000, 1500))

    # 暂停 2 秒
    sleep(2)

    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待 1 秒
    sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)  # 鼠标平滑移动到 (2870, 570)
    # 松开鼠标左键
    pyautogui.mouseUp(button='left')

    # 暂停 2 秒
    sleep(2)
    # 点击 (1414, 1214)
    pyautogui.click(1414, 1214, button='left')
    # 暂停 15 秒
    sleep(15)
    # 再次点击 (1414, 1214)
    pyautogui.click(1414, 1214, button='left')

    while True:
        ocr_tool.click_on_text('SKIP',region=(2394, 290, 272, 114),lang='en')
        if ocr_tool.check_text_exists('Shop',region=(1599, 1526, 304, 127),lang='en') is True:
            break

    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"文件 {json_file_path} 未找到。")
        return None
    except json.JSONDecodeError:
        logging.error(f"文件 {json_file_path} 不是有效的JSON。")
        return None

def init_tools(screenshot_path):
    ocr_tool = OCRClickTool(screenshot_path=screenshot_path)
    openCVClicker = OpenCVClicker(screenshot_path=screenshot_path)
    return ocr_tool, openCVClicker

def execute_task(json_file_path, screenshot_path):
    config = load_config(json_file_path)
    if config is None:
        return

    ocr_tool, openCVClicker = init_tools(screenshot_path)

    pre_order_traversal(config, ocr_tool=ocr_tool, openCVClicker=openCVClicker)

def rescue_mission():
    execute_task("minashigonoshigoto_json/rescue_mission.json", "./pic/screenshotOCR.png")

def event_task():
    execute_task("minashigonoshigoto_json/event_task.json", "./pic/screenshotOCR.png")

def daily_task():
    execute_task("minashigonoshigoto_json/daily_task.json", "./pic/screenshotOCR.png")


def pre_order_traversal(node,ocr_tool,openCVClicker):
    if node is not None:
        if 'recognition' in node:
            openCVClicker.routine_click(img_model_path=node['template'],region=node['region'])
        if 'text' in node:
            ocr_tool.click_on_text(target_text=node['text'],region=node['region'],lang=node['lang'])# 访问当前节点
        sleep(1)
        pre_order_traversal(node.get('left', None),ocr_tool,openCVClicker)  # 遍历左子树
        pre_order_traversal(node.get('right', None),ocr_tool,openCVClicker)  # 遍历右子树



# print("JSON中包含'next'字段:" if has_next else "JSON中不包含'next'字段.")
# login_bonus()
while True:
    event_task()