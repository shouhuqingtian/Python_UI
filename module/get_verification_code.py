# -*- coding: utf-8 -*-
# @Time    : 2024/9/20
# @Author  : Bin
# @Software: Aqua
# @File    : get_verification_code.py

import io
from PIL import Image

# from module.chaojiying import Chaojiying_Client

import module.chaojiying

def screenshots(driver):
    """
  截图验证码的方法，将验证码部分截图并保存到指定路径。

  :param driver: WebDriver实例，用于操控浏览器。
  """
    # 获取缩放比例
    scale = driver.execute_script("return window.devicePixelRatio;")

    captcha_element = driver.find_element(by="xpath", value='//div[@class="login-container-codeImg"]//img')

    # 获取验证码元素的真实坐标,尺寸
    location = captcha_element.location
    size = captcha_element.size
    x, y = location['x']*scale, location['y']*scale
    width, height = size['width']*scale, size['height']*scale

    # 截取整个浏览器的截图
    screenshot = driver.get_screenshot_as_png()

    # 使用Pillow加载截图
    image = Image.open(io.BytesIO(screenshot))

    # 裁剪验证码所在的区域
    captcha_image = image.crop((x, y, x + width, y + height))

    # 保存裁剪后的验证码图片
    captcha_image_path = "../test_ui_auto/picture/test.jpg"
    captcha_image.save(captcha_image_path)

    # 识别截取到的图片
    chaojiying_res = module.chaojiying.Chaojiying_Client('shouhuqingtian', '13691959110', '912169')	#用户中心>>软件ID 生成一个替换 96001
    im = open('../test_ui_auto/picture/test.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying_res.PostPic(im, 1902))

    # # 显示裁剪后的验证码图片
    # captcha_image.show()



