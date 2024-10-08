# -*- coding: utf-8 -*-
# @Time    : 2024/9/29
# @Author  : Bin
# @Software: Aqua
# @File    : test__sent_for_repair.py

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# driver = webdriver.Chrome()


def test_parts_repair(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'维修管理')]").click()
    driver.find_element(By.XPATH, "//li/span[text()='送修审批']").click()
    driver.find_element(By.CLASS_NAME, "el-icon-plus").click()
    driver.find_element(By.XPATH, "(//input[@placeholder='请选择'])[2]").click()
    sleep(10)
    # # 使用 JavaScriptExecutor 来执行你的 JavaScript 代码
    # js_code = """
    # var element = document.evaluate("(//span[contains(text(),'零部件修理')])[4]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    # element.click();
    # """
    #
    # # 执行 JavaScript 代码并点击元素
    # driver.execute_script(js_code)
    # driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(4)").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='单元体修理'])[6]/following::li[1]").click()


    # driver.find_element(By.XPATH, "(//span[contains(text(),'零部件修理')])[4]").click
    driver.find_element(By.XPATH, "(//span[contains(text(),'选择')])[3]").click()

    sleep(2)


