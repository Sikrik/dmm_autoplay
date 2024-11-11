import time
import cv2
import pyautogui
import os





class OpenCVClick:
    def __init__(self, screenshot_dir="./pic", screenshot_name="screenshot.png"):
        self.screenshot_dir = screenshot_dir
        self.screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def capture_screenshot(self, region=None):
        """
        截取屏幕指定区域的截图。
        :param region: 截图区域 (x, y, w, h)，默认为全屏
        :return: 截图路径，如果截图失败则返回 None
        """
        try:
            pyautogui.screenshot(region=region).save(self.screenshot_path)
            return self.screenshot_path
        except Exception as e:
            print(f"截图失败: {e}")
            return None

    def find_template_center(self, img_model_path, region=None, confidence_threshold=0.7):
        """
        在指定区域内匹配模板图片，并返回中心坐标。
        :param img_model_path: 模板图片路径
        :param region: 截图区域 (x, y, w, h)，默认为全屏
        :param confidence_threshold: 匹配的置信度阈值
        :return: 匹配区域的中心坐标（元组形式），匹配失败返回 None
        """
        screenshot_path = self.capture_screenshot(region)
        if not screenshot_path:
            return None

        # 读取截图和模板图片
        img = cv2.imread(screenshot_path)
        img_template = cv2.imread(img_model_path)

        if img is None or img_template is None:
            print(f"未能加载图像: {'截图' if img is None else '模板'}")
            return None

        # 模板匹配
        result = cv2.matchTemplate(img, img_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # 检查置信度是否达到阈值
        if max_val < confidence_threshold:
            print(f"匹配置信度不足（{max_val} < {confidence_threshold}），未找到目标")
            return None

        # 计算匹配区域的中心坐标
        height, width = img_template.shape[:2]
        center_x = max_loc[0] + width // 2
        center_y = max_loc[1] + height // 2
        if region:
            center_x += region[0]
            center_y += region[1]

        center_avg = (center_x, center_y)
        print(f"找到目标，中心坐标为: {center_avg}")
        return center_avg

    def auto_click(self, coordinates):
        """
        点击指定的坐标。
        :param coordinates: 坐标元组
        """
        if coordinates:
            pyautogui.click(coordinates[0], coordinates[1], button='left', duration=0.3)
            print(f"点击坐标: {coordinates}")
            time.sleep(1)
        else:
            print("坐标无效，未执行点击")

    def routine_click(self, img_model_path, name, region=None, confidence_threshold=0.8):
        """
        通用模板匹配和点击操作例程。
        :param img_model_path: 模板图片路径
        :param name: 操作名称（用于日志）
        :param region: 截图区域 (x, y, w, h)，默认为全屏
        :param confidence_threshold: 匹配的置信度阈值
        """
        coordinates = self.find_template_center(img_model_path, region=region, confidence_threshold=confidence_threshold)
        if coordinates:
            print(f"正在点击 {name}")
            self.auto_click(coordinates)
        else:
            print(f"未找到 {name}")



# 调用示例
if __name__ == "__main__":
    click_handler = OpenCVClick()
    click_handler.routine_click("./pic/terminal.png", '终端')
    click_handler.routine_click("./pic/terminal.png", '终端区域', region=(0, 240, 2800, 1400))
