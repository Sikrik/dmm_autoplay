import os
from time import sleep

import cv2
import pyautogui
from paddleocr import PaddleOCR

import loginbonus
from AutoClickerTools.OpenCVClick import OpenCVClick
from AutoClickerTools.GameAutoClick import GameAutoClick

images_directory = "./juru_pic"
screenshot_path = "./pic/screenshot.png"
openCVClick = OpenCVClick()
gameAutoClick = GameAutoClick()

# 全局初始化 OCR 对象，避免重复初始化
ocr = PaddleOCR(use_angle_cls=True, lang='japan', show_log=False)


def capture_screenshot():
    """截取屏幕指定区域并保存"""
    region = (0, 240, 2800, 1400)
    pyautogui.screenshot(region=region).save(screenshot_path)


def judgment_interface():
    """
    识别当前界面并返回界面名称
    """
    capture_screenshot()
    img2 = cv2.imread(screenshot_path)
    image_files = [f for f in os.listdir(images_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for img in image_files:
        try:
            result = pyautogui.locateCenterOnScreen(f"{images_directory}/{img}", confidence=0.9)
            if result:
                print(f"识别到界面: {img[:-4]}")
                return img[:-4]
        except Exception as e:
            print(f"识别界面时出现错误: {e}")
    print("未识别到任何匹配的界面")
    return None


def execute_task(task):
    """通用任务执行函数，减少代码冗余"""
    gameAutoClick.routine_click(f"{images_directory}/{task}.png", task)


def daily_task():
    """
    执行每日任务的操作
    """
    tasks = [
        "maoxian", "ziyuanshouji", "yikuoshouji", "queding", "ok", "qianbishouji",
        "yikuoshouji", "queding", "ok", "maoxian", "special_stage", "migong",
        "yikuoskip", "queding", "ok", "ok"
    ]
    for task in tasks:
        execute_task(task)


def main():
    """
    主循环，根据界面判断进行相应操作
    """
    count = 0
    while True:
        text = judgment_interface()
        if text == "navigation_bar_of_rescue_mission":
            execute_task("rescue_mission")
        elif text == "bp2":
            openCVClick.routine_click(f"{images_directory}/bp2.png", 'bp2', (2000, 500, 500, 800))
        elif text == "bp1":
            openCVClick.routine_click(f"{images_directory}/bp1.png", 'bp1', (2000, 500, 500, 800))
        elif text in ["tiaozhan", "fanhui"]:
            if count >= 2:
                execute_task("fanhui")
                execute_task("shuaxing")
                count -= 2
            else:
                execute_task("tiaozhan")
                count += 1
        elif text == "next":
            execute_task("next")
        elif text == "liberation":
            execute_task("liberation")
        elif text == "close":
            execute_task("close")
        else:
            print("未检测到已定义的界面，继续循环检查...")


# 执行每日任务和主操作
if __name__ == '__main__':
    # loginbonus.juruhuanxiangjizhan()
    # sleep(10)
    # daily_task()
    # sleep(10)
    # pyautogui.click(464, 1603, button='left', duration=2)
    main()
