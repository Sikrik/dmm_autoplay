import pyautogui
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemplateScreenClicker:
    def __init__(self, confidence=0.8, delay=0.5):
        """
        初始化模板屏幕点击器对象
        :param confidence: 模板匹配的置信度
        :param delay: 点击后的默认延迟时间（秒）
        """
        self.confidence = confidence
        self.delay = delay

    def locate_template(self, img_model_path):
        """
        在屏幕上定位模板图片的中心坐标
        :param img_model_path: 模板图片路径
        :return: 检测到的区域的中心坐标，未找到则返回 None
        """
        try:
            center_avg = pyautogui.locateCenterOnScreen(img_model_path, confidence=self.confidence)
            if center_avg:
                logging.info(f"在屏幕上找到目标 {img_model_path}，中心坐标为: {center_avg}")
            else:
                logging.info(f"未找到目标 {img_model_path}")
            return center_avg
        except Exception as e:
            logging.error(f"定位模板时出现错误: {e}")
            return None

    def execute_click(self, coordinates):
        """
        在指定坐标执行点击操作
        :param coordinates: 坐标元组
        """
        if coordinates:
            try:
                pyautogui.click(coordinates[0], coordinates[1], button='left', duration=1)
                logging.info(f"已点击坐标: x={coordinates[0]}, y={coordinates[1]}")
            except Exception as e:
                logging.error(f"执行点击时出现错误: {e}")
        else:
            logging.warning("坐标无效，未执行点击操作")

    def automated_clicking_process(self, img_model_path, target_name=None):
        """
        自动化点击流程，定位模板并执行点击
        :param img_model_path: 模板图片路径
        :param target_name: 点击目标的名称（用于日志）
        """
        coordinates = self.locate_template(img_model_path)
        if coordinates:
            logging.info(f'正在点击 {target_name}')
            self.execute_click(coordinates)
            time.sleep(self.delay)
        else:
            logging.info(f"未找到 {target_name}，跳过点击操作")

# 使用示例
if __name__ == "__main__":
    screen_clicker = TemplateScreenClicker(confidence=0.8, delay=2)
    screen_clicker.automated_clicking_process("../temporary_images/terminal.png", "终端")