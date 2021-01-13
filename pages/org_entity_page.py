from common.base_page import BasePage

class Org_Entity(BasePage):
    # 登入
    loc_1 = ("css", "span[title='监管智库']")
    loc_2 = ("css", "span[title='监管对象']")
    loc_3 = ("css", "span[title='机构类主体']")
    loc_4 = ("css", ".ant-table-thead [type='checkbox']")
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

    def org_tag(self):
        self.click(self.loc_1)
        self.click(self.loc_2)
        self.click(self.loc_3)
        self.click(self.loc_4)
        self.sleep(5)