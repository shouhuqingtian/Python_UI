# -*- coding: utf-8 -*-
# @Time    : 2024/9/29
# @Author  : Bin
# @Software: Aqua
# @File    : test__sent_for_repair.py
from sys import implementation

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# driver = webdriver.Chrome()


def test_parts_repair(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "(//span[contains(text(),'维修管理')])[1]").click()
    driver.find_element(By.XPATH, "//li/span[text()='送修审批']").click()
    driver.find_element(By.CLASS_NAME, "el-icon-plus").click()
    driver.find_element(By.XPATH, "(//input[@placeholder='请选择'])[2]").click()
    sleep(2)

    # 执行 JavaScript 代码并点击元素
    repair_option = driver.find_element(By.XPATH, "//div[@x-placement='bottom-start']//span[contains(text(),'零部件修理')]")
    driver.execute_script("arguments[0].click();", repair_option)
    # 选择库存ID
    driver.find_element(By.XPATH, "(//span[contains(text(),'选择')])[3]").click()
    driver.find_element(By.XPATH, "(//div)[1862]").click()
    driver.find_element(By.XPATH, "(//span[contains(text(),'确 定')])[12]").click()
    # 选择 Vendor
    driver.find_element(By.XPATH, "(//span[contains(text(),'选择')])[3]").click()
    driver.find_element(By.XPATH, "(//div[contains(text(),'--')])[214]").click()
    # 选择 Repair Party
    driver.find_element(By.XPATH, "(//input[contains(@placeholder,'请选择')])[3]").click()
    driver.find_element(By.XPATH, "(//li)[730]").click()
    # QTY输入1
    driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[14]").sendkey("1")
    driver.find_element(By.XPATH, "(//input[contains(@type,'number')])[2]").sendkey("1")
    # 保存并申请审批
    driver.find_element(By.XPATH, "(//span[contains(text(),'保存并申请审批')])[1]").click()



sleep(2)


