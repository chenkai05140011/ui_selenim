import time
from common.base_page import BasePage

class Tag(BasePage):
    # 登入
    loc_1 = ("xpath", "//span[@title='监管智库']")
    loc_2 = ("xpath", "(//span[@title='监管标签'])[1]")
    loc_3 = ("xpath", "(//span[@title='监管标签'])[2]")
    loc_4 = ("xpath", "//span[text()='禁毒管理']")
    loc_5 = ("xpath", "//button[@nz-wave='[object Object]']")
    loc_6 = ("xpath", "//span[text()='公安禁毒管理']")
    loc_7 = ("xpath", "(//input[@placeholder='请输入'])[1]")
    loc_8 = ("xpath", "//input[@type='checkbox']")
    loc_9 = ("xpath", "(//div[@unselectable='unselectable'])[1]")
    loc_10 = ("xpath", "(//li[@unselectable='unselectable'])[1]")
    loc_11 = ("xpath", "(//div[@class='ant-select-selection__rendered'])[2]")
    loc_12 = ("xpath", "(//input[@placeholder='请输入'])[2]")
    loc_13 = ("name", "textarea")
# 缺少自动标签部分
    loc_14 = ("xpath", "(//button[@nz-wave='[object Object]'])[2]")
    loc_17 = ("css", ".ant-message span")
    loc_15 = ("xpath", "//span[text()='陈凯一直自动标签 (1级) ']")
    loc_16 = ("xpath", "(//button[@nz-wave='[object Object]'])[3]")

    def click_tag(self):
        self.click(self.loc_1)
        self.click(self.loc_2)
        self.click(self.loc_3)
        self.click(self.loc_4)
        self.sleep(5)


    def add_tag(self, tagname="陈凯ui自动化新建标签", department="陈凯ui自动化责任处室", remarks="陈凯ui自动化备注"):
        self.click(self.loc_4)
        self.click(self.loc_5)
        self.type(self.loc_7, tagname)
        self.click(self.loc_8)
        self.click(self.loc_9)
        self.click(self.loc_10)
        self.type(self.loc_12, department)
        self.type(self.loc_13, remarks)
        self.click(self.loc_14)
        self.get_img()
        text = self.get_text(self.loc_17)
        return text

    def update_status_tag(self):
        self.click(self.loc_1)
        self.click(self.loc_2)
        self.click(self.loc_3)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web =Org_Entity(driver)
    web.open_url('http://ales.pre.icinfo.co/')
    driver.maximize_window()
    web.wait(10)
    web.click_tag()
    web.add_tag()
    time.sleep(10)
    web.quit()



