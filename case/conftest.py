from selenium import webdriver
import pytest
import time
from pages.login_page import LoginPage
import allure
from selenium.webdriver.chrome.options import Options

@allure.feature("设置driver")
@pytest.fixture(scope="session")
def driver(request):
    # # linux启动
    # chrome_options = Options()
    # chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    # chrome_options.add_argument('--headless')  # 无界面
    # chrome_options.add_argument('--no-sandbox')  # 解决devtoolsactiveport文件不存在报错
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')  # 禁用gpu硬件加速
    # _driver = webdriver.Chrome(chrome_options=chrome_options)
    # # 奇安信可信
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = r"C:\Users\kevin\AppData\Roaming\360se6\Application\360se.exe"  # 这里是360安全浏览器的路径
    # chrome_options.add_argument(r'--lang=zh-CN')  # 这里添加一些启动的参数
    # _driver = webdriver.Chrome(chrome_options=chrome_options)
    # window启动
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(5)
    _driver.maximize_window()

    def end():
        print("全部caes执行完退出游览器")
        time.sleep(5)
        _driver.quit()
    request.addfinalizer(end)
    return _driver

@allure.feature("用户登录")
@pytest.fixture(scope="function")
def login_cf(driver):
    web = LoginPage(driver)
    web.login()
    time.sleep(3)
    assert web.is_login_success()
    return driver