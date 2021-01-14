from selenium import webdriver
import pytest
import time
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver(request):
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(5)
    _driver.maximize_window()

    def end():
        print("全部caes执行完退出游览器")
        time.sleep(5)
        _driver.quit()
    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope="session")
def login_cf(driver):
    web = LoginPage(driver)
    web.login()
    return driver