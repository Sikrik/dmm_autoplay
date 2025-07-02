import json
import logging
from json import JSONDecodeError
from pathlib import Path
import cv2
import pyautogui
from PIL import Image
import os


def get_curr_folder_imgs_region_to_json(folder_path, screenshot_path):
  """
  从给定文件夹中读取图片，并使用模板匹配在界面上找到图片的位置。
  增删改查的增
  """
  json_path = Path(folder_path) / "currFolderImgs.json"
  pyautogui.screenshot().save(screenshot_path)

  try:
    with open(json_path, 'r') as f:
      data = json.load(f)
  except FileNotFoundError:
    data = {"images": []}  # 初始化数据结构
  except JSONDecodeError:
    data = {"images": []}

  img_basenames = {file_base_name(img['img_path']) for img in data["images"]}

  for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".png")):
      file_path = os.path.join(folder_path, filename)
      if file_base_name(file_path) in img_basenames:
        continue  # 如果图片已存在，跳过

      with Image.open(file_path) as img:
        img_interface = cv2.imread(screenshot_path)
        img_template = cv2.imread(file_path)
        h, w = img_template.shape[:2]
        result = cv2.matchTemplate(img_interface, img_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val < 0.8:
          continue

        x, y, ww, hh = max_loc[0] - 25, max_loc[1] - 50, w + 50, h + 75
        print(f"匹配到文件{filename}, 置信度{max_val}, 修改后的识别范围为({x}, {y}, {ww}, {hh})")
        new_data = {
          "img_path": norm_path(file_path),
          "region": (x, y, ww, hh)
        }
        data["images"].append(new_data)

  with open(json_path, 'w') as f:
    json.dump(data, f)  # 美化输出

  logging.info(f'Data has been written to {json_path}')


def mod_reg(task_json, currFolderImags_json):
  """
  更新并保存任务的区域信息。
  """
  with open(task_json, 'r', encoding='utf-8') as file:
    daily_task_data = json.load(file)

  with open(currFolderImags_json, 'r', encoding='utf-8') as file:
    curr_folder_imgs_data = json.load(file)

  update_region(daily_task_data, curr_folder_imgs_data)

  with open(task_json, 'w', encoding='utf-8') as file:
    json.dump(daily_task_data, file, ensure_ascii=False)

  print(f"更新完成，结果已保存到{task_json}文件中。")


def norm_path(original_path):
  """标准化路径"""
  return str(Path(original_path).resolve())


def file_base_name(original_path):
  """提取文件名"""
  return os.path.basename(original_path)


def update_region(node, images):
  """更新daily_task_data中template对应的region"""
  if node is None:
    logging.warning("Node is None")
    return
  if 'template' in node:
    for img in images['images']:
      if file_base_name(node['template']) == file_base_name(img['img_path']):
        logging.info(f"开始更新task_json中的{node['template']}，对应currFolderImgs中的{img['img_path']}")
        node['region'] = img['region']
        break

  if 'left' in node and node['left'] is not None:
    update_region(node['left'], images)

  if 'right' in node and node['right'] is not None:
    update_region(node['right'], images)


if __name__ == '__main__':
  get_curr_folder_imgs_region_to_json(folder_path="../juru/juru_pic/rescue_mission", screenshot_path="../juru/temporary_images/tools_screenshot.png")
  # mod_reg(task_json="../juru/juru_json/daily_migong.json", currFolderImags_json="../juru/juru_pic/migong/currFolderImgs.json")
