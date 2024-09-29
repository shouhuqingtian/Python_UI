# -*- coding: utf-8 -*-
# @Time    : 2024/9/29
# @Author  : Bin
# @Software: Aqua
# @File    : test__sent_for_repair.py
from ast import Bytes

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_parts_repair():
    driver.find_element(By.XPATH, "//li/span[text()='送修审批']")
    driver.find_element(By.CLASS_NAME, "")

