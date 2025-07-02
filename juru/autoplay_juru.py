import logging
from time import sleep
from AutoClickerTools.OpenCVClicker import OpenCVClicker
from AutoClickerTools.dmm_autoplay import AutoplayDMMGame

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Autoplayjuru(AutoplayDMMGame):

    def login_bonus(self):
        self.execute_task("juru_json/login_bonus.json")

    def rescue_mission(self):
        while self.find_template(template_path="./juru_pic/rescue_mission/quxiao.png",region=(1011, 1316, 410, 195)):
            self.execute_task("juru_json/rescue_mission.json")

    def daily_task(self):
        self.execute_task("juru_json/daily_task.json")

    def daily_free_gacha(self):
        self.execute_task("juru_json/daily_free_gacha.json")

    def daily_migong(self):
        self.execute_task("juru_json/daily_migong.json")

    def daily_shop(self):
        self.execute_task("juru_json/daily_shop.json")

    def expedition(self):
        self.execute_task("juru_json/expedition.json")

    def paiqian(self):
        self.execute_task("juru_json/paiqian.json")

autoplayjuru = Autoplayjuru()

# autoplayjuru.login_bonus()
# sleep(10)


# autoplayjuru.paiqian()
# autoplayjuru.daily_task()
# sleep(10)
# autoplayjuru.daily_migong()
# sleep(10)
# autoplayjuru.daily_shop()
# sleep(10)
# autoplayjuru.daily_free_gacha()
# sleep(10)
autoplayjuru.rescue_mission()
