from selenium.webdriver.common.by import By


# page_url = www.baidu.com
class Page(object):
    def __init__(self, driver):
        self.driver = driver

