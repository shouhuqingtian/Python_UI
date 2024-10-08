#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from module.get_verification_code import screenshots
from testcase.test__sent_for_repair import test_parts_repair


class TestWebsite:
  # 1. Check browser configuration in browser_setup_and_teardown
  # 2. Run 'Selenium Tests' configuration
  # 3. Test report will be created in reports/ directory

  @pytest.fixture(autouse=True)
  def browser_setup_and_teardown(self):
    self.use_selenoid = False  # set to True to run tests with Selenoid

    if self.use_selenoid:
      self.browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={
          "browserName": "chrome",
          "browserSize": "1920x1080"
        }
      )
    else:
      self.browser = webdriver.Chrome()

    self.browser.maximize_window()
    self.browser.implicitly_wait(10)
    self.browser.get("http://192.168.16.50:10006/login?redirect=%2Fassets%2FminimumInventory%3Ftype%3Dnav/")

    yield

    self.browser.close()
    self.browser.quit()

  def test_tools_menu(self):
    """this test checks presence of Developer Tools menu item"""
    tools_menu = self.browser.find_element(By.NAME,
                                           "username")
    # 登录后台管理系统
    tools_menu.send_keys("dev")
    menu_popup = self.browser.find_element(By.NAME, "password")
    menu_popup.send_keys("air2021")
    self.browser.find_element(By.NAME, "verifyCode").click()
    code = screenshots(self.browser)
    self.browser.find_element(By.NAME, "verifyCode").send_keys(code)
    self.browser.find_element(By.XPATH, "//button/span[text()='Login']").click()

    # 验证是否登录成功，登录成功后会显示刷新按钮
    refresh_button = self.browser.find_element(By.XPATH, "//span[text()='刷新']")
    assert refresh_button.is_displayed(),  "登录失败，用户头像没有显示。"

    # 执行零部件维修测试用例
    test_parts_repair(self.browser)

  def test_navigation_to_all_tools(self):
    """this test checks navigation by See All Tools button"""
    see_all_tools_button = self.browser.find_element(By.CSS_SELECTOR, "a.wt-button_mode_primary")
    see_all_tools_button.click()

    products_list = self.browser.find_element(By.ID, "products-page")
    assert products_list is not None
    assert self.browser.title == "All Developer Tools and Products by JetBrains"

  def test_search(self):
    """this test checks search from the main menu"""
    search_button = self.browser.find_element(By.CSS_SELECTOR, "[data-test='site-header-search-action']")
    search_button.click()

    search_field = self.browser.find_element(By.CSS_SELECTOR, "[data-test='search-input']")
    search_field.send_keys("Selenium")

    submit_button = self.browser.find_element(By.CSS_SELECTOR, "button[data-test='full-search-button']")
    submit_button.click()

    search_page_field = self.browser.find_element(By.CSS_SELECTOR, "input[data-test='search-input']")
    assert search_page_field.get_property("value") == "Selenium"