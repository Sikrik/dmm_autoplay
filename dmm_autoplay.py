import json
from time import sleep
import logging
import pyautogui
from AutoClickerTools.OCRClickTool import OCRClickTool
from AutoClickerTools.OpenCVClicker import OpenCVClicker
import tkinter as tk
from tkinter import messagebox




class AutoplayDMMGame:
    def __init__(self, screenshot_path="./pic/screenshotOCR.png"):
        self.ocr_tool = OCRClickTool(lang="ch", screenshot_path=screenshot_path)
        self.screenshot_path = screenshot_path
        self.openCVClicker = OpenCVClicker(screenshot_path=self.screenshot_path)
        self.config_cache = {}

    @staticmethod
    def swipe(start_pos=(2870, 520), end_pos=(2870, 570)):
        pyautogui.mouseDown(x=start_pos[0], y=start_pos[1], button='left')
        pyautogui.moveTo(x=end_pos[0], y=end_pos[1], duration=1)
        pyautogui.mouseUp(button='left')

    def load_config(self, json_file_path):
        if json_file_path in self.config_cache:
            return self.config_cache[json_file_path]
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                config = json.load(file)
                self.config_cache[json_file_path] = config
                return config
        except FileNotFoundError:
            logging.error(f"文件 {json_file_path} 未找到。")
        except json.JSONDecodeError:
            logging.error(f"文件 {json_file_path} 不是有效的JSON。")
        return None

    def execute_task(self, json_file_path):
        config = self.load_config(json_file_path)
        if config is None:
            return
        self.pre_order_traversal(config)


    @staticmethod
    def popup_message():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("完成", "程序执行结束！")
        root.destroy()

    def pre_order_traversal(self, node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current:
                if self.execute_node(current):
                    # 如果execute_node返回True，则先执行左节点
                    stack.extend([current.get('left'), current.get('right')])
                else:
                    # 如果execute_node返回False，则先执行右节点
                    stack.extend([current.get('right'), current.get('left')])

    def execute_node(self, node):
        if node is None:
            logging.info("执行节点为空，跳过。")
            return

        try:
            if 'recognition' in node:
                self._execute_recognition(node)
            elif 'text' in node:
                self._execute_text(node)
            elif 'swipe' in node:
                self._execute_swipe(node)
            elif 'click' in node:
                self._execute_click(node)
            else:
                logging.warning(f"未知的节点类型: {node}")
        except Exception as e:
            logging.error(f"执行节点时发生错误：{e}")

        if 'waiting_time' in node:
            sleep(node.get('waiting_time', 0))

    def _execute_recognition(self, node):
        logging.info("执行识别操作")
        return self.openCVClicker.routine_click(img_model_path=node['template'], region=node['region'])

    def _execute_text(self, node):
        logging.info("执行文本点击操作")
        return self.ocr_tool.click_on_text(target_text=node['text'], region=node['region'], lang=node['lang'])

    def _execute_swipe(self, node):
        logging.info("执行滑动操作")
        self.swipe(start_pos=node['start_pos'], end_pos=node['end_pos'])

    @staticmethod
    def _execute_click(node):
        logging.info("执行点击操作")
        pyautogui.moveTo(x=node['x'], y=node['y'])
        pyautogui.click(x=node['x'], y=node['y'])