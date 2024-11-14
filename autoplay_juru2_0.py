import time
from time import sleep

import pyautogui

from AutoClickerTools2.OCRClickTool import OCRClickTool
from AutoClickerTools2.OpenCVClicker import OpenCVClicker
import json



def juruhuanxiangjizhan():
    # 初始化 OCR 以避免多次重复加载
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")

    # 查找并点击目标文本 'dmm'
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')

    # 查找并点击目标文本 '巨乳幻想激战'
    ocr_tool.click_on_text('巨乳幻想激战', region=(1392, 160, 1000, 1500), lang='ch')

    # 等待 2 秒
    sleep(2)

    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待 1 秒
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)  # 鼠标平滑移动到 (2870, 570)
    # 松开鼠标左键
    pyautogui.mouseUp(button='left')

    # 等待 10 秒
    sleep(10)

    # 点击 (1414, 1214) 位置
    pyautogui.click(1414, 1214, button='left', duration=1)

    # 等待 20 秒
    sleep(20)

    while True:
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        if ocr_tool.check_text_exists('ミッション', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()

def juruhuanxiangjizhanjiuyuanzhan():
    ocr_tool = OCRClickTool(screenshot_path="./pic/screenshotOCR.png")
    json_file_path = "juru_json/juru_challenge.json"
    # 打开文件并读取JSON数据
    with open(json_file_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    operation = None
    while True:
        for action in config['actions']:
            if ocr_tool.check_text_exists(action['text'], region=action['region'], lang=action['lang']):
                if operation == action['text']:
                    if ocr_tool.check_text_exists('取消', region=(1041, 1340, 352, 132), lang='japan'):
                        ocr_tool.click_on_text('取消', region=(1041, 1340, 352, 132), lang='japan')
                        ocr_tool.click_on_text(action['back']['text'], region=action['back']['region'],
                                               lang=action['back']['lang'])
                        ocr_tool.click_on_text("ホーム", region=(331, 1530, 250, 170), lang='japan')
                        return
                    ocr_tool.click_on_text(action['back']['text'], region=action['back']['region'],
                                           lang=action['back']['lang'])
                    opencvclicker = OpenCVClicker(screenshot_path="./pic/OpenCV_screenshot.png")
                    sleep(2)
                    opencvclicker.routine_click(action['back']['next_action'], region=action['back']['next_region'])
                else:
                    ocr_tool.click_on_text(action['text'], region=action['region'], lang=action['lang'])
                    operation = action['text']


def daily_task():
    ocr_tool = OCRClickTool(screenshot_path="./pic/screenshotOCR.png")
    json_file_path = "juru_json/juru_daily_task.json"
    # 打开文件并读取JSON数据
    with open(json_file_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
        count = 0
    while True:
        for action in config['actions']:
            if action['text'] == '<':
                openCVClicker = OpenCVClicker(screenshot_path="./pic/OpenCV_screenshot.png")
                openCVClicker.routine_click(action['template'], region=action['region'])
            elif ocr_tool.click_on_text(action['text'], region=action['region'], lang=action['lang']) is True:
                sleep(2)
            else:
                continue
juruhuanxiangjizhanjiuyuanzhan()


