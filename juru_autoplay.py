import pyautogui
import os
import time
from AutoClickerTools import ClickByOCR #使用OCR识别图片中的文字并点击 未封装
from AutoClickerTools.GameAutoClick import GameAutoClick #直接定位屏幕中指定图片的坐标并点击
from AutoClickerTools.OpenCVClick import OpenCVClick
from dmm_autoplay import dmm_autoplay
import psutil




class juru_autoplay(dmm_autoplay):

    game_region = (0, 240, 2800, 1400)#截取屏幕的指定区域x,y,w,h,此数值为不截到chrome的上面部分的区域
    screenshot_path = "./pic/juru_autoplay.png"#截取屏幕区域后保存的地址
    images_directory = "./juru_pic"#该游戏的根图片文件夹
    confidence = 0.9 #图片识别的置信度阈值


    def login_bonus(self):
        """
        登录并领取登录奖励       已完成
        :return:
        """
        # 初始化 OCR 以避免多次重复加载
        ClickByOCR.init_ocr(lang='ch')
        # 查找并点击目标文本 'dmm'
        ClickByOCR.find_and_click_text('dmm', region=(2180, 160, 1000, 1500), lang='en')
        # 查找并点击目标文本 '巨乳幻想激战'
        ClickByOCR.find_and_click_text('巨乳幻想激战', region=(2180, 160, 1000, 1500), lang='ch')
        time.sleep(2)
        #拖动侧边栏
        pyautogui.mouseDown(x=2870, y=520, button='left')
        time.sleep(2)
        pyautogui.mouseUp(button='left')

        # 等待 20 秒
        time.sleep(10)
        while True:
            interface = self.judgment_interface()
            if interface == "主页":
                break
            elif interface == "公告页面1" or interface == "公告页面2":
                ClickByOCR.find_and_click_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
                time.sleep(2)
            else:
                pyautogui.click(1500,1200,button='left', duration=1)
            time.sleep(2)

        # 使用完毕后手动释放 OCR 内存
        ClickByOCR.release_ocr()


    def daily_task(self):
        pass

    def repeatedly_challenge_rescue_mission(self):
        """
        反复挑战救援战
        :return:
        """
        # 初始化GameAutoClick
        game_auto_click = GameAutoClick()
        count = 0  # 记录点击挑战按钮的次数
        # 定义界面对应的操作
        interface_actions = {
            "主页": lambda: ClickByOCR.find_and_click_text("救援戦", region=(1440, 900, 1440, 900), lang='japan'),
            "救援战页面": lambda: ClickByOCR.find_and_click_text("bp2", region=(1440, 900, 1440, 900), lang='en'),
            "战斗准备页面": lambda: self._battle_preparation_page(count, game_auto_click),
            "挑战结果页面": lambda: ClickByOCR.find_and_click_text("次へ", region=(1440, 900, 1440, 900), lang='japan'),
            "战斗后的奖励领取页面1": lambda: ClickByOCR.find_and_click_text("解放", region=(1440, 900, 1440, 900),lang='japan'),
            "战斗后的奖励领取页面2": lambda: ClickByOCR.find_and_click_text("閉じる", region=(1440, 900, 1440, 900),lang='japan'),
        }

        # 反复进行挑战操作
        while True:
            # 获取当前进程的ID
            pid = os.getpid()

            # 获取进程对象
            process = psutil.Process(pid)

            # 获取内存信息（以MB为单位）
            memory_info = process.memory_info()
            print(f"当前进程使用的内存: {memory_info.rss / (1024 * 1024)} MB")
            # 检测bp值如果为1或0以下则break
            bp_value = ClickByOCR.find_value(region=(2221, 1647, 50, 53))  # 改下数值
            if bp_value <= 1:
                break

            # 获取判断出的当前页面的名称
            interface = self.judgment_interface()

            # 执行对应的操作
            action = interface_actions.get(interface)
            if action:
                action()

    def _battle_preparation_page(self, count, game_auto_click):
        """
        处理战斗准备页面的逻辑
        :param count: 点击挑战按钮的次数
        :param game_auto_click: 游戏自动点击对象
        :return: None
        """
        if count >= 2:
            ClickByOCR.find_and_click_text("戻る", region=(1440, 900, 1440, 900), lang='japan')
            time.sleep(2)
            game_auto_click.routine_click("./juru_pic/rescue_mission/refresh.png", "刷新救援战列表")
            count = 0
        else:
            ClickByOCR.find_and_click_text("挑戦", region=(1440, 900, 1440, 900), lang='japan')
            count += 1

    def clickOnElement(self):
        openCVClick = OpenCVClick()
        openCVClick.routine_click(f"{self.images_directory}/bp2.png", 'bp2', (2000, 500, 500, 800))
        pass

    def judgment_interface(self):
        """
        通过判断识别到的图片判断游戏中所处的场景        已完成
        添加场景时添加字典page_conditions即可
        识别文件夹为根图片文件夹中的judgment_interface
        :return: 字符串page
        """

        matched_images = self.judgment_imgs(directory="judgment_interface")

        # 定义条件和对应页面名称的字典
        page_conditions = {
            "主页": ["navigation_bar_of_home_page", "rescue_mission"],
            "救援战页面": ["navigation_bar_of_rescue_mission", "bp1", "bp2"],
            "战斗准备页面": ["battle_navigation_bar"],
            "挑战结果页面": ["challenge_results", "next"],
            "战斗后的奖励领取页面1": ["liberation", "challenge_results"],
            "战斗后的奖励领取页面2": ["close", "challenge_results"],
            "冒险页面": ["material", "stadium"],
            "资源收集页面": ["regor_collect", "elixir_collect"],
            "资源收集确认页面": ["regor_collect", "elixir_collect", "resource_collection_confirmation"],
            "资源收集报酬确认页面": ["resource_collection_reward_confirmation_page", "ok"],
            "公告页面1": ["close2", "notice"],
            "公告页面2": ["close2", "event_info"]
        }

        # 遍历字典，检查是否匹配相应的页面
        for page, conditions in page_conditions.items():
            if all(item in matched_images for item in conditions):
                print(f"\n当前画面正处于{page}")
                return page

        # 如果没有匹配的页面，返回 None 或默认页面
        print("\n当前画面无法匹配")
        return None

    def judgment_imgs(self,directory = None):
        """
        截取屏幕指定区域并保存并输出无文件后缀的文件名     已完成
        :param directory: juru_pic中的文件夹名称 如judgment_interface，文件夹名前不需要加/
        :return: 识别到的图片
        """
        # 截图并保存
        pyautogui.screenshot(region=self.game_region).save(self.screenshot_path)

        # 遍历文件夹并与屏幕截图所匹配
        if directory is None:
            image_files = [f for f in os.listdir(f"{self.images_directory}")
                           if f.endswith(('.png', '.jpg', '.jpeg'))]
        else:
            image_files = [f for f in os.listdir(f"{self.images_directory}/{directory}")
                           if f.endswith(('.png', '.jpg', '.jpeg'))]

        # 用于存储识别到的图片名字
        matched_images = []

        # 遍历每个图片文件并匹配
        for img in image_files:
            try:
                if directory is None:#判断是否是否有指定juru_pic下的文件夹
                    img_path = os.path.join(self.images_directory, img)# 构建文件路径
                else:
                    img_path = os.path.join(f"{self.images_directory}/{directory}", img)  # 构建文件路径
                print(img_path)
                result = pyautogui.locateCenterOnScreen(img_path, confidence=self.confidence)
                if result:
                    # print(f"识别到图片: {img}")
                    matched_images.append(img[:-4])  # 去掉文件扩展名
            except Exception as e:
                pass
                # print(f"未识别到图片{img}")

        # 输出匹配结果
        if matched_images:
            print("识别到的所有图片：",end="")
            for img in matched_images:
                print(f"{img}", end="\t")
            return matched_images
        else:
            print("未识别到任何匹配的界面")
            return []


#juru_autoplay = juru_autoplay()
# while True:
#     current_interface = juru_autoplay.judgment_interface()
#     if current_interface == "主页":
#         break
#     elif current_interface == "公告页面1" or current_interface == "公告页面2":
#         ClickByOCR.find_and_click_text('閉じる', region=(200, 240, 2400, 1400), lang='japan')
#         time.sleep(2)
# juru_autoplay.clickOnElement()
# juru_autoplay.judgment_interface()
# ClickByOCR.find_and_click_text("戻る",region=(1440, 900, 1440, 900), lang='japan')