import time
import cv2
import pyautogui
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OpenCVClicker:
    def __init__(self, screenshot_path = None, confidence_threshold=0.8):
        self.screenshot_path = screenshot_path
        self.confidence_threshold = confidence_threshold


    def capture_screenshot(self, region=None):
        """截取屏幕指定区域的截图。"""
        try:
            pyautogui.screenshot(region=region).save(self.screenshot_path)
            logging.info("截图成功")
            return self.screenshot_path
        except Exception as e:
            logging.error(f"截图失败: {e}")
            return None

    def find_template_center(self, img_model_path, region=None):
        """在指定区域内匹配模板图片，并返回中心坐标。"""
        screenshot_path = self.capture_screenshot(region)
        if not screenshot_path:
            return None

        img = cv2.imread(screenshot_path)
        img_template = cv2.imread(img_model_path)

        if img is None:
            logging.error("未能加载截图图像")
            return None
        if img_template is None:
            logging.error("未能加载模板图像")
            return None

        result = cv2.matchTemplate(img, img_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val < self.confidence_threshold:
            logging.warning(f"匹配置信度不足（{max_val} < {self.confidence_threshold}），未找到目标")
            return None

        height, width = img_template.shape[:2]
        center_x = max_loc[0] + width // 2
        center_y = max_loc[1] + height // 2
        if region:
            center_x += region[0]
            center_y += region[1]

        logging.info(f"找到目标，中心坐标为: ({center_x}, {center_y})")
        return (center_x, center_y)

    def auto_click(self, coordinates):
        """点击指定的坐标。"""
        if coordinates:
            try:
                pyautogui.moveTo(coordinates[0], coordinates[1])
                pyautogui.click(button='left', duration=0.3)
                logging.info(f"点击坐标: {coordinates}")
                time.sleep(0.5)
            except Exception as e:
                logging.error(f"点击时出现错误: {e}")
        else:
            logging.warning("坐标无效，未执行点击")

    def routine_click(self, img_model_path, name=None, region=None):
        """通用模板匹配和点击操作例程。"""
        coordinates = self.find_template_center(img_model_path, region=region)
        if coordinates:
            logging.info(f"正在点击 {name}")
            self.auto_click(coordinates)
        else:
            logging.info(f"未找到 {name}")

# 调用示例
if __name__ == "__main__":
    click_handler = OpenCVClicker()
    click_handler.routine_click("../pic/terminal.png", '终端')
    click_handler.routine_click("../pic/terminal.png", '终端区域', region=(0, 240, 2800, 1400))