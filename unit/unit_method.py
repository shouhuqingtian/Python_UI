# -*- coding: utf8 -*-
import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# 启动浏览器
def open_broswer(url):
    s = Service(executable_path=R'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)


# 读取CSV文件
def open_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        data = csv.reader(f)
        rows = [row for row in data]
        new_rows = rows[0::]
        return [item for i in new_rows for item in i]


# 定位元素,传入对象，定位方式，定位路径
def loc_element(driver, loc, loc_path):
    driver.find_element(loc, loc_path)
