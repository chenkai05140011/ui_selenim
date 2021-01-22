import time
import allure
from common.base_page import BasePage

@allure.feature("岗位类别管理")
class Job_Manage(BasePage):
    # 登入
    loc_1 = ("css", "span[title=监管智库]")
    loc_2 = ("css", "span[title=执法人员]")
    loc_3 = ("css", "span[title=岗位类别管理]")

    @allure.step("点击岗位类别管理菜单")
    def click_job_menu(self):
        self.click(self.loc_1)
        self.click(self.loc_2)
        self.click(self.loc_3)

    loc_add_job = ("css", ".operate button")  # 添加岗位类别按钮
    loc_job_name = ("css", "[formcontrolname=JobCategoryName]")  # 岗位类别名称
    loc_job_line = ("css", ".modal-content .tree-input")  # 适用条线
    loc_job_line_1 = ("css", "ul.ant-tree nz-tree-node:nth-child(1) i")  # 选择条线1
    loc_job_line_2 = ("css", ".ant-radio-input")  # 选择条线2
    loc_job_explain = ("css", "[formcontrolname=instructions]")  # 说明
    loc_job_y = ("css", ".ant-modal-footer button:nth-child(2)")  # 确定
    loc_job_n = ("css", ".ant-modal-footer button:nth-child(1)")  # 取消
    loc_alert = ("css", ".ant-message span")  # 验证是否添加成功

    @allure.step("添加岗位类别")
    def add_job(self, name="zdh_岗位类别名称", explain="zdh_说明"):
        self.click(self.loc_add_job)
        self.type(self.loc_job_name, name)
        self.click(self.loc_job_line)
        self.click(self.loc_job_line_1)
        self.click(self.loc_job_line_2)
        self.type(self.loc_job_explain, explain)
        self.click(self.loc_job_y)
        self.get_img()
        text = self.get_text(self.loc_alert)
        return text

    loc_edit_job = ("css", ".ant-table-tbody tr:nth-child(1) .table-handle a:nth-child(1)")  # 编辑岗位类别按钮
    loc_job_line_1_1 = ("css", "ul.ant-tree nz-tree-node:nth-child(2) i")  # 选择条线1
    loc_job_line_2_1 = ("css", ".ant-radio-input")  # 选择条线2

    @allure.step("修改岗位类别")
    def edit_job(self, name="zdh_岗位类别名称_edit", explain="zdh_说明_edit"):
        self.click(self.loc_edit_job)
        self.clear(self.loc_job_name)
        self.type(self.loc_job_name, name)
        self.click(self.loc_job_line)
        self.click(self.loc_job_line_1_1)
        self.click(self.loc_job_line_2_1)
        self.clear(self.loc_job_explain)
        self.type(self.loc_job_explain, explain)
        self.click(self.loc_job_y)
        self.get_img()
        text = self.get_text(self.loc_alert)
        return text

    loc_disabled_job = ("css", ".ant-table-tbody tr:nth-child(1) .table-handle a:nth-child(2)")  # 禁用岗位类别按钮
    loc_disabled_job_y = ("css", ".ant-modal-footer button:nth-child(1)")  # 禁用岗位类别按钮_确定
    loc_disabled_job_n = ("css", ".ant-modal-footer button:nth-child(2)")  # 禁用岗位类别按钮_取消

    @allure.step("启用停用岗位类别")
    def disabled_job(self):
        self.click(self.loc_disabled_job)
        self.get_img()
        self.click(self.loc_disabled_job_y)
        text = self.get_text(self.loc_alert)
        return text

    loc_details_job = ("css", ".ant-table-tbody tr:nth-child(1) .table-handle a:nth-child(3)")  # 详情岗位类别按钮
    loc_details_job_alert = ("css", ".ant-modal-title .ng-star-inserted")  # 验证进入详情
    loc_details_job_y = ("css", ".ant-modal-footer .ant-btn-primary")  # 详情岗位类别确定

    @allure.step("岗位类别详情")
    def details_job(self):
        self.click(self.loc_details_job)
        self.get_img()
        text = self.get_text(self.loc_details_job_alert)
        self.click(self.loc_details_job_y)
        return text

    loc_search_job_name = ("css", ".form-wrap [placeholder=请输入]")  # 岗位类别名称输入
    loc_search_job_y = ("css", ".search-area .ant-btn-primary")  # 查询按钮
    loc_search_job_assert = ("css", ".ant-table-tbody tr:nth-child(1) td:nth-child(2)")  # 验证查询结果

    @allure.step("岗位类别查询")
    def search_job(self, name="交通工程质监"):
        self.type(self.loc_search_job_name, name)
        self.click(self.loc_search_job_y)
        self.get_img()
        text = self.get_text(self.loc_search_job_assert)
        return text
