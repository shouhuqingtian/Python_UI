# -*- coding: utf-8 -*-
# @Time    : 2024/9/20
# @Author  : Bin
# @Software: Aqua
# @File    : get_verification_code.py

import io
import os
from lib2to3.pgen2 import driver

from PIL import Image


def screenshots(driver):
    """
  截图验证码的方法，将验证码部分截图并保存到指定路径。

  :param driver: WebDriver实例，用于操控浏览器。
  """
    # 定义固定的保存路径
    save_path = "../picture/a.jpg"

    # 获取当前文件所在目录的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 将相对路径转换为绝对路径
    save_path = os.path.abspath(os.path.join(base_dir, save_path))

    # 获取目标目录
    directory = os.path.dirname(save_path)

    # 如果目录不存在，创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"目录 {directory} 已创建。")

    # 打印完整的保存路径以便调试
    print(f"完整的保存路径: {save_path}")

    # 确保 save_path 是一个完整的文件路径
    if not save_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        raise ValueError(f"保存路径必须包含文件名和扩展名，比如 'a.jpg' 或 'a.png'。当前路径: {save_path}")

    captcha_element = driver.find_element(by="xpath", value='//div[@class="login-container-codeImg"]//img')

    # 获取验证码元素的坐标,尺寸
    location = captcha_element.location
    size = captcha_element.size
    x, y = location['x'], location['y']
    width, height = size['width'], size['height']

    # 截取整个浏览器的截图
    screenshot = driver.get_screenshot_as_png()

    # 使用Pillow加载截图
    image = Image.open(io.BytesIO(screenshot))

    # 裁剪验证码所在的区域
    captcha_image = image.crop((x, y, x + width, y + height))

    # 保存裁剪后的验证码图片
    captcha_image_path = "../picture/a.jpg"
    captcha_image.save(captcha_image_path)
    print(f"验证码截图已保存: {captcha_image_path}")

    # 显示裁剪后的验证码图片
    captcha_image.show()



