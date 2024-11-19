import logging

from dmm_autoplay import AutoplayDMMGame

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Autoplayjuru(AutoplayDMMGame):

    def login_bonus(self):
        self.execute_task("juru_json/login_bonus.json")

    def rescue_mission(self):
        while True:
            if self.ocr_tool.check_text_exists("取消",region=(1024, 1327, 383, 151)):
                self.popup_message()
                return
            self.execute_task("juru_json/rescue_mission.json")

    def daily_task(self):
        self.execute_task("juru_json/daily_task.json")


Autoplayjuru = Autoplayjuru()
#Autoplayjuru.login_bonus()
#pyautogui.screenshot(region=(1460, 1489, 360, 131)).save("./screenshotOCR_test.png")
#Autoplayjuru.daily_task()
Autoplayjuru.rescue_mission()
