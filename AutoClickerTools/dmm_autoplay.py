import json
import re
from time import sleep
import logging
import pyautogui
from AutoClickerTools.OCRClickTool import OCRClickTool
from AutoClickerTools.OpenCVClicker import OpenCVClicker
import tkinter as tk
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor


class AutoplayDMMGame:
  def __init__(self, screenshot_path="./temporary_images/screenshot.png"):
    """
    初始化函数，用于设置OCR和OpenCV共用的截图位置，并初始化相关工具。

    :param screenshot_path: OCR和OpenCV共用的截图位置，默认为"./temporary_images/screenshot.png"
    """
    # 初始化OCR工具，指定语言为中文和截图路径
    self.ocr_tool = OCRClickTool(lang="ch", screenshot_path=screenshot_path)
    # 保存截图路径为实例变量
    self.screenshot_path = screenshot_path
    # 初始化OpenCV点击工具，使用相同的截图路径
    self.openCVClicker = OpenCVClicker(screenshot_path=self.screenshot_path)
    # 初始化配置缓存字典，用于存储可能的配置信息，以提高效率
    self.config_cache = {}
    self.executor = ThreadPoolExecutor(max_workers=2)  # 根据实际情况调整 max_workers


  @staticmethod
  def swipe(start_pos=(2870, 520), end_pos=(2870, 570)):
    """
    滑动操作
    :param start_pos: 滑动时鼠标的起始坐标
    :param end_pos: 滑动时鼠标的终止坐标
    :return:
    """
    pyautogui.mouseDown(x=start_pos[0], y=start_pos[1], button='left')
    pyautogui.moveTo(x=end_pos[0], y=end_pos[1], duration=1)
    pyautogui.mouseUp(button='left')

  def load_json(self, json_file_path):
    """
    加载json配置文件
    :param json_file_path: path of json
    :return:
    """
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
    """
    检查json是否存在并执行任务
    :param json_file_path:json文件地址
    :return:
    """
    config = self.load_json(json_file_path)
    if config is None:
      logging.error("无法加载配置文件。")
      return
    self.pre_order_traversal(config)


  @staticmethod
  def popup_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("完成", "程序执行结束！")
    root.destroy()

  def pre_order_traversal(self, node):
    """
    获取原始节点进行前序遍历
    :param node: 当前节点，从该节点开始进行前序遍历
    :return: 无返回值，但可能会根据遍历结果执行某些操作
    """
    # 检查传入的节点是否为空
    if not node:
      logging.info("传入的节点为空，跳过。")
      return

    # 初始化栈，用于辅助进行前序遍历
    stack = [node]
    while stack:
      current = stack.pop()
      if current:
        try:
          # 根据当前节点的执行结果决定先遍历左子节点还是右子节点
          if self.execute_node(current):
            # 如果execute_node返回True，则先执行左节点
            if current.get('left'):
              stack.append(current.get('left'))
            if current.get('right'):
              stack.append(current.get('right'))
          else:
            # 如果execute_node返回False，则先执行右节点
            if current.get('right'):
              stack.append(current.get('right'))
            if current.get('left'):
              stack.append(current.get('left'))
        except Exception as e:
          # 处理execute_node可能抛出的异常
          logging.error(f"Error executing node: {e}")
          # 可以选择继续处理或中断遍历
          continue

  def execute_node(self, node):
    """
    解析节点的动作并执行
    :param node:
    :return:
    """
    if node is None or not isinstance(node, dict):
      logging.warning("执行节点为空或不是字典，跳过。")
      return

    try:
      if 'action' in node:
        action = node['action']
        for action_type in ['click', 'swipe']:
          if action_type in action:
            getattr(self, f"_execute_{action_type}")(node)
      elif 'recognition' in node:
        self._execute_recognition(node)
      elif 'text' in node:
        self._execute_text(node)
      else:
        logging.warning(f"未知的节点类型: {node}")
    except KeyError as ke:
      logging.error(f"键错误: {ke}")
      raise  # 重新抛出异常，以便上层处理
    except Exception as e:
      logging.error(f"执行节点时发生错误：{e}", exc_info=True)
      raise  # 重新抛出异常，以便上层处理

    waiting_time = node.get('waiting_time', 0)
    if isinstance(waiting_time, (int, float)) and waiting_time >= 0:
      sleep(waiting_time)
    else:
      logging.warning("等待时间无效，跳过等待。")
      raise ValueError("等待时间必须是非负的整数或浮点数")  # 抛出异常，确保无效等待时间不会被忽略


  def _execute_recognition(self, node):
    logging.info("执行识别图片并点击的操作")
    return self.openCVClicker.routine_click(img_model_path=node['template'], region=node['region'])

  def _execute_text(self, node):
    logging.info("执行文本点击操作")
    return self.ocr_tool.click_on_text(target_text=node['text'], region=node['region'], lang=node['lang'])

  def _execute_swipe(self, node):
    logging.info("执行滑动操作")
    self.swipe(start_pos=node['start_pos'], end_pos=node['end_pos'])


  @staticmethod
  def _execute_click(node):
    logging.info(f"执行点击操作，坐标: ({node['x']}, {node['y']})")
    screen_width, screen_height = pyautogui.size()
    if 'x' not in node or 'y' not in node:
      logging.error("节点数据不完整，缺少 x 或 y 坐标")
      return
    x, y = node['x'], node['y']
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
      logging.error(f"坐标 ({x}, {y}) 超出屏幕范围")
      return
    try:
      pyautogui.moveTo(x, y)
      pyautogui.click(x, y)
    except Exception as e:
      logging.error(f"执行点击操作时发生错误: {e}")


  def _check_bp(self, minimum_bp, region):
    """
    :param minimum_bp: 最小bp值，当小于此值返回false
    :param region: 区域参数
    :return: BP值是否小于最小值
    """
    try:
        result = self.ocr_tool.find_numeric_value(region=region)
    except Exception as e:
        logging.error(f"在调用 OCR 工具时发生异常: {e}")
        return False

    if result is None:
        logging.error("OCR 工具返回了 None，无法解析 BP 值")
        return True

    try:
        match = re.match(r"^(\d+)", str(result))
        if match:
            value = int(match.group(1))
        else:
            logging.error("正则表达式匹配失败，无法解析 BP 值")
            return True
    except ValueError:
        logging.error("解析 BP 值时发生错误")
        return False

    if value <= minimum_bp:
        logging.info("BP已小于规定值")
        self.popup_message()
        return False
    else:
        logging.info("BP值正常")
        return True
  def find_template(self,template_path,region):
    return self.openCVClicker.find_template(template_path,region)
