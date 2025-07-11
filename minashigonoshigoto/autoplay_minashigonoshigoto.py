import logging
from AutoClickerTools.dmm_autoplay import AutoplayDMMGame

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AutoplayMinashigoto(AutoplayDMMGame):


    def login_bonus(self):
        self.execute_task("minashigonoshigoto_json/login_bonus.json")

    def daily_task(self):
        self.execute_task("minashigonoshigoto_json/daily_task.json")

    def rescue_mission(self):
        while self._check_bp(10,region=(1842, 320, 134, 68)):
            self.execute_task("minashigonoshigoto_json/rescue_mission.json")

    def event_task(self):
        while self._check_bp(10,region=(1842, 320, 134, 68)):
            self.execute_task("minashigonoshigoto_json/event_task.json",)

    def event_girotomission(self):
        while self._check_bp(10,region=(1842, 320, 134, 68)):
            self.execute_task("minashigonoshigoto_json/girutomission.json")



# 使用示例
if __name__ == "__main__":
    auto_clicker = AutoplayMinashigoto()
    #auto_clicker.login_bonus()
    # auto_clicker.daily_task()
    # auto_clicker.rescue_mission()
    auto_clicker.event_task()
    # auto_clicker.event_girotomission()
