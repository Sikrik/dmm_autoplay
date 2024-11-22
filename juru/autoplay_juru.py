import logging

from AutoClickerTools.dmm_autoplay import AutoplayDMMGame

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Autoplayjuru(AutoplayDMMGame):

    def login_bonus(self):
        self.execute_task("juru_json/login_bonus.json")

    def rescue_mission(self):
        while self._check_bp(1,region=(1531, 280, 110, 80)):
            self.execute_task("juru_json/rescue_mission.json")

    def daily_task(self):
        self.execute_task("juru_json/daily_task.json")

    def daily_free_gacha(self):
        self.execute_task("juru_json/daily_free_gacha.json")

    def daily_migong(self):
        self.execute_task("juru_json/daily_migong.json")

    def daily_shop(self):
        self.execute_task("juru_json/daily_shop.json")


autoplayjuru = Autoplayjuru()
#autoplayjuru.login_bonus()
#autoplayjuru.daily_task()
#autoplayjuru.daily_migong()
#autoplayjuru.daily_shop()
#autoplayjuru.daily_free_gacha()
autoplayjuru.rescue_mission()
