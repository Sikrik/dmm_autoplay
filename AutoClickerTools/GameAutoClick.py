import gc
import time
import pyautogui

class GameAutoClick:
    def __init__(self, confidence=0.8, delay=0.5):
        """
        初始化GameAutoClick对象
        :param confidence: 模板匹配的置信度
        :param delay: 点击后的默认延迟时间（秒）
        """
        self.confidence = confidence
        self.delay = delay

    def get_coordinates(self, img_model_path):
        """
        获取模板图片在屏幕上的中心坐标
        :param img_model_path: 模板图片路径
        :return: 检测到的区域的中心坐标，未找到则返回 None
        """
        try:
            center_avg = pyautogui.locateCenterOnScreen(img_model_path, confidence=self.confidence)
            if center_avg:
                print(f"在屏幕上找到目标 {img_model_path}，中心坐标为: {center_avg}")
            else:
                print(f"未找到目标 {img_model_path}")
            return center_avg
        except Exception as e:
            print(f"获取坐标时出现错误: {e}")
            return None

    def click_at(self, coordinates):
        """
        在指定坐标点击
        :param coordinates: 坐标元组
        """
        if coordinates:
            try:
                pyautogui.click(coordinates[0], coordinates[1], button='left',duration=1)
                print(f"已点击坐标: x={coordinates[0]}, y={coordinates[1]}")
            except Exception as e:
                print(f"点击坐标时出现错误: {e}")
        else:
            print("坐标无效，未执行点击操作")

    def routine_click(self, img_model_path, name=None):
        """
        自动化点击例程，获取坐标并点击
        :param img_model_path: 模板图片路径
        :param name: 点击项目名称（用于日志）
        """
        coordinates = self.get_coordinates(img_model_path)
        if coordinates:
            print(f'正在点击 {name}')
            self.click_at(coordinates)
            time.sleep(self.delay)
        else:
            print(f"未找到 {name}，跳过点击操作")
        gc.collect()

# 使用示例
if __name__ == "__main__":
    click_handler = GameAutoClick(confidence=0.8, delay=2)
    click_handler.routine_click("./pic/terminal.png", "终端")
