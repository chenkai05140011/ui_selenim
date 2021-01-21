import time
from common.base_page import BasePage
import allure

@allure.feature("执法人员管理")
class ZF_People(BasePage):
    # 登入
    loc_1 = ("css", "span[title=监管智库]")
    loc_2 = ("css", "span[title=执法人员]")
    loc_3 = ("css", "span[title=执法人员库]")
    loc_4 = ("css", "span[title=岗位类别管理]")

    loc_6 = ("xpath", "(//button[@nz-wave='[object Object]'])[1]")  # 查询
    loc_7 = ("css", ".search-area button:nth(1)")  # 重置
    loc_8 = ("css", ".search-area button:nth(2)")  # 更多
    loc_9 = ("css", "input[placeholder=请输入用户名查询]")
    loc_9_1 = ("xpath", "//td[text()='陈凯']")
    loc_10 = ("css", "input[placeholder=请输入手机号]")
    # 缺少其他查询条件细节处以后补上

    # 添加人员元素
    loc_5 = ("css", ".operate button")  # 添加人员按钮
    loc_11 = ("css", "input[placeholder=请输入手机号查询]")  # 添加人员输入手机号
    loc_11_1 = ("css", ".ant-breadcrumb")# 添加人员输入手机号-确认
    loc_12 = ("css", "[nzplaceholder=请选择人员类别]")  # 人员类别
    loc_13 = ("css", "[nzplaceholder=请选择学历]")  # 学历
    loc_14 = ("css", "[nzplaceholder=请选择执法状态] ")  # 是否日常执法
    loc_15 = ("xpath", "(//li[@unselectable='unselectable'])[2]")  # 选择执法人员
    loc_16 = ("css", ".ant-select-dropdown-menu-vertical li:nth(2)")  # 选择辅助人员
    loc_17 = ("xpath", "(//li[@unselectable='unselectable'])[2]")  # 是
    loc_18 = ("css", ".ng-tns-c13-1194 li:nth(2)")  # 否
    loc_19 = ("css", ".tree-input-top")  # 岗位类别
    loc_20 = ("css", "input[placeholder=搜索]")  # 搜索岗位类别
    loc_21 = ("css", ".ng-star-inserted .ant-tree-checkbox-inner")  # 勾选岗位类别
    loc_22 = ("css", ".search-area .ant-btn-primary")  # 勾选岗位类别确认
    loc_23 = ("css", ".ng-tns-c13-1194 li:nth(2)")  # 勾选岗位类别取消
    #添加执法证
    loc_24 = ("css", ".operate button")  # 添加执法证
    loc_25 = ("css", ".back-wrapper [nztype=default]")  # 返回
    loc_26 = ("css", ".back-wrapper [nztype=primary]")  # 保存
    loc_27 = ("css", "[formcontrolname=zfCertNo]")  # 执法证编号
    loc_28 = ("css", "[formcontrolname=certType]")  # 执法类别
    loc_29 = ("css", "[formcontrolname=zfArea]")  # 执法区域
    loc_30 = ("css", ".ant-checkbox")  # 有效期 长期有效
    loc_31 = ("css", ".ant-modal-footer .ant-btn-primary")  # 添加执法证 确定
    loc_32 = ("css", ".ant-modal-footer .ant-btn-default")  # 添加执法证 取消
    loc_33 = ("css", ".ant-message span")  # 验证是否添加成功

    loc_list_more = ("css", ".table-handle button")  # 列表更多
    loc_list_del = ("link", "删除")  # 删除
    loc_list_del_y = ("css", ".ant-modal-footer .ant-btn-primary")  # 确定删除
    loc_list_edit = ("css", ".ant-table-tbody tr .table-handle a:nth-child(1)")  # 编辑
    loc_list_details = ("link", "详情")  # 详情
    loc_list_edit_zf_del = ("css", ".ant-table-tbody tr .ant-table-td-right-sticky a")  # 删除执法证
    loc_list_edit_zf_del_y = ("css", ".ant-modal-footer .ant-btn-primary")  # 删除执法证确定
    loc_list_disabled = ("css", ".table-handle a:nth-child(2)")  # 禁用
    loc_list_disabled_y = ("css", ".ant-modal-footer .ant-btn-primary")  # 确定禁用

    @allure.step("进入执法人员菜单")
    def click_zf_menu(self):
        self.click(self.loc_1)
        self.click(self.loc_2)
        self.click(self.loc_3)

    @allure.step("添加执法人员")
    def add_zf_people(self, phone="13186977800", search="测试岗位类别", zfCertNo="陈凯ui自动化zfCertNo", certType="陈凯ui自动化certType",zfArea="陈凯ui自动化zfArea"):
        self.click(self.loc_5)
        self.type(self.loc_11, phone)
        self.click(self.loc_11_1)
        self.click(self.loc_12)
        self.click(self.loc_15)
        self.click(self.loc_19)
        # self.type(self.loc_20, search)
        self.click(self.loc_21)
        self.click(self.loc_22)
        self.click(self.loc_14)
        self.click(self.loc_17)
        self.click(self.loc_24)
        self.type(self.loc_27, zfCertNo)
        self.type(self.loc_28, certType)
        self.type(self.loc_29, zfArea)
        self.click(self.loc_30)
        self.click(self.loc_31)
        self.click(self.loc_26)
        text = self.get_text(self.loc_33)
        return text

    @allure.step("查询执法人员")
    def search_fz_people(self, name='陈凯'):
        self.clear(self.loc_10)
        self.type(self.loc_9, name)
        self.click(self.loc_6)
        text = self.get_text(self.loc_9_1)
        return text

    @allure.step("删除执法人员")
    def del_fz_people(self, phone='13186977800'):
        self.clear(self.loc_10)
        self.type(self.loc_10, phone)
        self.click(self.loc_6)
        self.move_to_element(self.loc_list_more)
        self.click(self.loc_list_del)
        self.click(self.loc_list_del_y)

    @allure.step("启用停用执法人员")
    def disabled_fz_people(self, phone='13186977800'):
        self.clear(self.loc_10)
        self.type(self.loc_10, phone)
        self.click(self.loc_6)
        self.sleep(3)
        self.click(self.loc_list_disabled)
        self.click(self.loc_list_edit_zf_del_y)
        text = self.get_text(self.loc_list_disabled)
        return text

    @allure.step("修改执法人员")
    def edit_fz_people(self, phone='13186977800', zfCertNo="编辑陈凯ui自动化zfCertNo", certType="编辑陈凯ui自动化certType",zfArea="编辑陈凯ui自动化zfArea"):
        self.clear(self.loc_10)
        self.type(self.loc_10, phone)
        self.click(self.loc_6)
        self.sleep(2)
        self.click(self.loc_list_edit)
        self.click(self.loc_24)
        self.type(self.loc_27, zfCertNo)
        self.type(self.loc_28, certType)
        self.type(self.loc_29, zfArea)
        self.click(self.loc_30)
        self.click(self.loc_31)
        self.click(self.loc_list_edit_zf_del)
        self.click(self.loc_list_edit_zf_del_y)
        self.click(self.loc_26)
        text = self.get_text(self.loc_33)
        return text

    @allure.step("详情执法人员")
    def details_fz_people(self, phone='13186977800'):
        self.clear(self.loc_10)
        self.type(self.loc_10, phone)
        self.click(self.loc_6)
        self.move_to_element(self.loc_list_more)
        self.click(self.loc_list_details)

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



