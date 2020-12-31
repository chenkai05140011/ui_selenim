from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest


class Test_webui:
    def __init__(self):

        # 在启动浏览器时加入配置
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 打开
        self.driver.get('http://ales.fat3.icinfo.co/')
        #隐试等待
        self.driver.implicitly_wait(3)
    def test_uizdh(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]').send_keys("15868385402")
        # 显示等待
        # WebDriverWait(self.driver, 10).until()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]').send_keys("aa112233.")
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.sidebar-nav__item-text[title="监管智库"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.sidebar-nav__item-text[title="监管标签"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-id="77"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ng-tns-c21-54.ng-tns-c21-46.ng-star-inserted').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ant-btn.ng-star-inserted.ant-btn-primary').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入"]').send_keys("zdh_标签1")
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'nz-select[nzplaceholder="请选择"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item.ng-star-inserted').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入"]').send_keys("zdh_标签1责任处室")
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入备注"]').send_keys("zdh_标签1说明")
        self.driver.find_element(By.CSS_SELECTOR, 'button[nztype="primary"]').click()

        time.sleep(5)
        self.driver.quit()
if __name__ == '__main__':
    re = Test_webui()
    re.test_uizdh()

