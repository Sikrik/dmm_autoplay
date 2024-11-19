import time
from time import sleep
import pyautogui
from AutoClickerTools.OCRClickTool import OCRClickTool


"""
一键领取领取游戏中的登陆奖励
"""


def miwuliecheshaonv():
    # 初始化 OCR 以避免多次重复加载
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")

    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')

    ocr_tool.click_on_text('迷雾少女列车', region=(1392, 160, 1000, 1500), lang='ch')

    # 等待 10 秒
    sleep(10)

    # 点击 (1440, 900)
    pyautogui.click(1440, 900, button='left')

    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()
    sleep(20)


def guerdegongzuo():
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
    time.sleep(2)
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

    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


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


def shanyaoxingqishi():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    # 查找并点击 'dmm' 和 '闪耀星骑士'
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('闪耀星骑士', region=(1392, 160, 1000, 1500), lang='ch')

    # 暂停 2 秒
    sleep(2)

    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')

    # 等待一会儿
    time.sleep(2)

    # 平滑移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)

    # 松开鼠标左键
    pyautogui.mouseUp(button='left')

    # 暂停 7 秒
    time.sleep(10)

    # 点击指定位置两次
    while True:
        pyautogui.click(x=1420, y=1300, button='left', duration=1)
        time.sleep(2)
        if ocr_tool.check_text_exists("MENU", region=(1730, 257, 265, 70), lang='en'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def deepone():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    # 第一步：查找并点击 'dmm' 和 'DeepOne'
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('DeepOne', region=(1392, 160, 1000, 1500), lang='en')

    # 暂停 2 秒
    sleep(2)

    # 鼠标拖动操作：按住、移动并松开
    pyautogui.mouseDown(x=2870, y=520, button='left')
    sleep(2)
    pyautogui.moveTo(2870, 550, duration=1)
    pyautogui.mouseUp(button='left')

    # 点击指定位置 (1424, 1131) 多次，间隔 15 秒
    time.sleep(15)
    pyautogui.click(x=1424, y=1131, button='left', duration=1)
    time.sleep(15)
    pyautogui.click(x=1424, y=1131, button='left', duration=1)
    time.sleep(15)
    pyautogui.click(x=1424, y=1131, button='left', duration=1)

    # 循环点击 “SKIP” 和 “閉じる”，直到找到 “ガチャ”
    while True:
        ocr_tool.click_on_text('SKIP', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        if ocr_tool.check_text_exists('ガチャ', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def chuanqisiyecao():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('传奇四叶草', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 590, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    pyautogui.mouseUp(button='left')
    sleep(20)
    while True:
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        pyautogui.click(x=2600, y=468, button='left', duration=1)
        if ocr_tool.check_text_exists('ギルド', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def tianqibeilun():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('天启悖论', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 590, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('SKIP', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        if ocr_tool.check_text_exists('Rank', region=(200, 240, 2400, 1400), lang='en'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def yaoguailuanwu():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('妖怪乱舞', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(15)
    while True:
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        if ocr_tool.check_text_exists('閑催中', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def tianshilianjie():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='en')
    ocr_tool.click_on_text('天使链接', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    while True:
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('とじる', region=(200, 240, 2400, 1400), lang='japan')
        if ocr_tool.check_text_exists('スタミナ', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def shaonvyishuqitan():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('少女艺术奇谭', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 590, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.click(x=1424, y=1536, button='left', duration=1)
        sleep(2)
        if ocr_tool.check_text_exists('ネーロ', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def qiannianzhanzheng():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('干年战争', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    while True:
        pyautogui.mouseDown(x=1418, y=1000, button='left')
        sleep(2)
        pyautogui.mouseUp(button='left')
        sleep(2)
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        if ocr_tool.check_text_exists('ランク', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def tonghuabianjing():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('童话边境', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.mouseDown(x=1418, y=1000, button='left')
        sleep(2)
        pyautogui.mouseUp(button='left')
        sleep(2)
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        sleep(2)
        if ocr_tool.check_text_exists('Rank', region=(200, 240, 2400, 1400), lang='en'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def mid_night_girls():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('MidNightGirls', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('GAME START', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        sleep(2)
        if ocr_tool.check_text_exists('イベント', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def guaiwunvhai():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('怪物女孩', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 550, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        pyautogui.click(x=1424, y=1131, button='left', duration=1)
        sleep(2)
        ocr_tool.click_on_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
        sleep(2)
        if ocr_tool.check_text_exists('ガチャ', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def xianzhelianmeng():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('贤者联盟', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 570, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        # pyautogui.click(x=2573, y=356, button='left', duration=1)
        # sleep(2)
        pyautogui.click(x=1424, y=1170, button='left', duration=1, clicks=2)
        sleep(2)
        # ocr_tool.click_on_text('OK', region=(200, 240, 2400, 1400), lang='en')
        # sleep(2)
        pyautogui.click(x=1424, y=1567, button='left', duration=1, clicks=2)
        sleep(2)

        ocr_tool.click_on_text('x', region=(200, 240, 2400, 1400), lang='en')
        sleep(2)
        if ocr_tool.check_text_exists('Rank', region=(200, 240, 2400, 1400), lang='en'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


def tangguochongtu():
    ocr_tool = OCRClickTool(lang="ch", screenshot_path="./pic/screenshotOCR.png")
    ocr_tool.click_on_text('dmm', region=(1392, 160, 1000, 1500), lang='ch')
    ocr_tool.click_on_text('糖果冲突', region=(1392, 160, 1000, 1500), lang='ch')
    sleep(2)
    # 按住鼠标左键
    pyautogui.mouseDown(x=2870, y=520, button='left')
    # 等待一会儿
    time.sleep(2)
    # 移动鼠标
    pyautogui.moveTo(2870, 590, duration=1)  # 鼠标平滑移动到 (400, 500)
    # 松开鼠标左键
    sleep(2)
    pyautogui.mouseUp(button='left')
    sleep(2)
    while True:
        pyautogui.click(x=1424, y=1567, button='left', duration=1, clicks=2)
        sleep(2)
        ocr_tool.click_on_text('OK', region=(924, 674, 987, 585), lang='en')
        sleep(2)
        ocr_tool.click_on_text('SKIP', region=(200, 240, 2600, 600), lang='en')
        sleep(2)
        if ocr_tool.check_text_exists('ガチャ', region=(200, 240, 2400, 1400), lang='japan'):
            break
    # 使用完毕后手动释放 OCR 内存
    ocr_tool.release_resources()


if __name__ == '__main__':
    # miwuliecheshaonv()#有问题
    # guerdegongzuo()
    # juruhuanxiangjizhan()
    xianzhelianmeng()# 稍有问题
    tianqibeilun()
    mid_night_girls()#稍有问题 免费十连
    deepone()
    tangguochongtu()
    guaiwunvhai()
    tonghuabianjing()#shaoyouwenti/
    qiannianzhanzheng()
    shaonvyishuqitan()
    tianshilianjie()
    yaoguailuanwu()
    chuanqisiyecao()
    shanyaoxingqishi()
