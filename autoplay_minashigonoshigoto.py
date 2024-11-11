import os
import pyautogui
from AutoClickerTools.OpenCVClick import OpenCVClick
from AutoClickerTools.GameAutoClick import GameAutoClick

# 配置路径
images_directory = "./minashigonoshigoto_pic"
screenshot_path = "./pic/screenshot.png"
openCVClick = OpenCVClick()
gameAutoClick = GameAutoClick()

def take_screenshot():
    """
    捕获当前屏幕并保存为临时文件
    """
    pyautogui.screenshot(screenshot_path)
    return screenshot_path

def judgment_interface():
    """
    识别当前界面并返回界面名称
    """
    take_screenshot()
    image_files = [f for f in os.listdir(images_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    for img in image_files:
        try:
            result = pyautogui.locateCenterOnScreen(f"{images_directory}/{img}", confidence=0.8)
            if result:
                print(f"识别到界面: {img[:-4]}")
                return img[:-4]
        except Exception as e:
            None
    print("未识别到任何匹配的界面")
    return None

def main(max_retries=5):
    """
    主循环，尝试识别界面并执行对应操作
    """
    for count in range(1, max_retries + 1):
        text = judgment_interface()
        if text:
            print(f"检测到界面: {text}")
            execute_action(text)
        else:
            print("未检测到界面，继续检查...")

def execute_action(action):
    """
    根据界面名称执行对应的操作
    """
    action_func = actions.get(action)
    if action_func:
        try:
            action_func()
        except Exception as e:
            print(f"执行 {action} 操作时出错: {e}")
    else:
        print(f"未定义的动作: {action}")

# 定义界面操作函数
def help():
    gameAutoClick.routine_click("minashigonoshigoto_pic/help.png", "救援一栏")

def canzhan():
    gameAutoClick.routine_click("minashigonoshigoto_pic/canzhan.png", "参战")

def jueding():
    gameAutoClick.routine_click("minashigonoshigoto_pic/jueding.png", "决定")

def chuji():
    gameAutoClick.routine_click("minashigonoshigoto_pic/chuji.png", "出击")

def zhandoujieshu():
    gameAutoClick.routine_click("minashigonoshigoto_pic/zhandoujieshu.png", "战斗结束")
    pyautogui.click(2600, 500, button='left')

def cigihe():
    gameAutoClick.routine_click("minashigonoshigoto_pic/cigihe.png", "下一")

def fuhuo():
    gameAutoClick.routine_click("minashigonoshigoto_pic/fuhuo.png", "复活")
    pyautogui.click(1600, 1350, button='left')

def guanbi():
    gameAutoClick.routine_click("minashigonoshigoto_pic/guanbi.png", "关闭")

def cigikuesuto():
    gameAutoClick.routine_click("minashigonoshigoto_pic/cigikuesuto.png", "下一关卡")

def ok():
    gameAutoClick.routine_click("minashigonoshigoto_pic/ok.png", "ok")

# 界面到函数的映射
actions = {
    "help": help,
    "canzhan": canzhan,
    "jueding": jueding,
    "chuji": chuji,
    "zhandoujieshu": zhandoujieshu,
    "cigihe": cigihe,
    "fuhuo": fuhuo,
    "guanbi": guanbi,
    "cigikuesuto": cigikuesuto,
    "ok": ok
}

# 启动主函数
if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("程序已终止")
