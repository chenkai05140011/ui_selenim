from common.base_page import BasePage
import allure


@allure.feature("登入模块")
class LoginPage(BasePage):
    # 登入
    loc_1 = ("css", 'input[placeholder="请输入用户名"]')
    loc_2 = ("css", 'input[placeholder="请输入密码"]')
    loc_3 = ("css", 'input[placeholder="请输入验证码"]')
    loc_4 = ("css", "button[type=submit]")
    loc_5 = ("css", "span[title=首页]")

    @allure.step("输入用户名")
    def input_user(self, username):
        self.type(self.loc_1, username)

    @allure.step("输入密码")
    def input_psw(self, psw):
        self.type(self.loc_2, psw)

    @allure.step("输入验证码")
    def input_yzm(self, yzm):
        self.type(self.loc_3, yzm)

    @allure.step("点击登录按钮")
    def click_button(self):
        self.click(self.loc_4)

    @allure.step("验证是否登入成功")
    def is_login_success(self):
        self.get_img()
        text = self.get_text(self.loc_5)
        print(text)
        return text == "首页"

    @allure.step("登录")
    def login(self, url='http://59.202.63.108/v2/#/passport/login', username='15868385402', psw='1', yzm='1'):
        self.open_url(url)
        self.input_user(username)
        self.input_psw(psw)
        self.input_yzm(yzm)
        self.click_button()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web =LoginPage(driver)
    web.open_url('http://ales.pre.icinfo.co/')
    driver.maximize_window()
    web.login('18395948730', '1', '1')
    web.wait(3)
    result = web.is_login_success()
    web.quit()



