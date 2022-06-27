import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 读取电话号码，循环登录
def open_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        data = csv.reader(f)
        rows = [row for row in data]
        new_rows = rows[3::]
        return [item for i in new_rows for item in i]


# 打开浏览器
def open_broswer(url, username, password):
    s = Service(executable_path=R'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(8)
    driver.get(url)
    time.sleep(3)

    # 定位元素，添加匹配车型
    driver.find_element(By.ID, 'userName').send_keys(username)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
    print("用户名是",username)
    driver.find_element(By.CLASS_NAME, 'text-14').click()
    time.sleep(3)
    driver.get(
        'https://staging-h5-pc-41.nanxinwang.com/v5.10.6/index.php?client=PC#!/index/storeManagement/invenTory/invenToryManager')
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="shopManagement"]/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//dd/button[@class="x-button btn-medium x-button--normal btn-line-blue"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//span[contains(text(), "添加车型")]').click()
    driver.find_element(By.XPATH, '//li/p[contains(text(), "大众")]').click()
    driver.find_element(By.XPATH, '//div/p[normalize-space(text())= "宝来"]').click()
    driver.find_element(By.XPATH, '//img[@src="http://img.nanxinwang.com/bsm/model/3927.png"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="mainWindow"]/div[2]/div/main/div/div/div[5]/button').click()
    # driver.find_element(By.XPATH, '//*[@id="shopInfo"]/div/div[3]/button').click()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    result = open_csv_file(R'C:\Users\heyij\Desktop\phone500.csv')
    for i in range(300):
        open_broswer(R'https://staging-h5-pc-41.nanxinwang.com/v5.10.6/index.php?client=PC#!/login', result[448+i], 123456)
        print(f"第{i+448}次循环")


