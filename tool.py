from PIL import Image
import os


def get_last_two_images_dimensions(folder_path):
    # 确保提供的路径存在且是一个目录
    if not os.path.isdir(folder_path):
        return "提供的路径不是一个有效的文件夹"

    # 获取文件夹中所有文件的列表，并过滤出图片文件
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # 按文件名排序，确保最后两个文件在列表的末尾
    images.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # 获取最后两个图片文件的路径
    last_two_images = images[-2:]
    last_image = images[-1:]

    # 创建一个字典来存储图片的路径和对应的宽高
    dimensions = []

    # 遍历最后两个图片文件
    for image in last_two_images:
        image_path = os.path.join(folder_path, image)
        try:
            # 打开图片并获取尺寸
            with Image.open(image_path) as img:
                width, height = img.size
                dimensions.append(width)
                dimensions.append(height)
        except IOError:
            # 如果文件不是图片，跳过
            print(f"无法打开图片文件：{image_path}")

    return dimensions


# 使用示例
folder_path = 'C:\\Users\\81209\\Pictures\\Screenshots'
print(get_last_two_images_dimensions(folder_path))