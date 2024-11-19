
import logging
from concurrent.futures import ThreadPoolExecutor

from dmm_autoplay import AutoplayDMMGame

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AutoplayMinashigoto(AutoplayDMMGame):


    def login_bonus(self):
        self.execute_task("minashigonoshigoto_json/login_bonus.json")

    def daily_task(self):
        self.execute_task("minashigonoshigoto_json/daily_task.json")

    def rescue_mission(self):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.ocr_tool.find_numeric_value, [1874, 321, 50, 48])
            while True:
                value = future.result()
                if value is not None and value < 10:
                    self.popup_message()
                    return
                self.execute_task("minashigonoshigoto_json/rescue_mission.json")

    def event_task(self):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.ocr_tool.find_numeric_value, [1874, 321, 80, 48])
            while True:
                value = future.result()
                if value is not None and value < 10:
                    self.popup_message()
                    return
                self.execute_task("minashigonoshigoto_json/event_task.json",)



# 使用示例
if __name__ == "__main__":
    auto_clicker = AutoplayMinashigoto()
    #auto_clicker.login_bonus()
    #auto_clicker.daily_task()
    #auto_clicker.rescue_mission()
    auto_clicker.event_task()
