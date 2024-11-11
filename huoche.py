import gc
import os
import time
import cv2
import pyautogui
from AutoClickerTools import GameAutoClick as opencv

images_directory = "./huoche_pic"


def judgment_interface():
    """
    识别当前界面，返回匹配图片的名称（不含扩展名），若无匹配则返回 None
    """
    image_files = [f for f in os.listdir(images_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    pyautogui.screenshot(region=(0, 240, 2800, 1400)).save("./pic/screenshot.png")  # 捕获屏幕截图以便匹配
    screenshot = cv2.imread("./pic/screenshot.png")

    for img in image_files:
        try:
            result = pyautogui.locateCenterOnScreen(f"{images_directory}/{img}", confidence=0.8)
            if result:
                print(f"识别到界面: {img[:-4]}")
                return img[:-4]  # 返回文件名去掉扩展名部分
        except Exception as e:
            print(f"识别界面时出现错误: {e}")

    print("未识别到任何匹配的界面")
    return None


def main():
    """
    主循环，根据识别的界面名称调用对应的处理函数
    """
    actions = {
        "ok": ok,
        "skip": skip,
        "zaichouyici": zaichouyici,
    }

    count = 0
    while count < 5:
        text = judgment_interface()
        if text in actions:
            actions[text]()  # 执行与识别到的界面对应的操作
            count += 1  # 计数操作次数
        else:
            print("无匹配操作，继续检测...")

        gc.collect()
        time.sleep(1)  # 添加适当的延迟，防止过度调用


def ok():
    """点击 'ok' 按钮"""
    opencv.routine("huoche_pic/ok.png", "ok")


def skip():
    """点击 'skip' 按钮"""
    opencv.routine("huoche_pic/skip.png", "skip")


def zaichouyici():
    """点击 '再抽一次' 按钮"""
    opencv.routine("huoche_pic/zaichouyici.png", "zaichou")


# 开始主流程
main()