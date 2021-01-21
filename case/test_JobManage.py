import pytest
import allure
from pages.JobManage_page import Job_Manage

@allure.epic("行政执法项目")
@allure.feature("执法人员管理")
@pytest.mark.ui_test
class Test_Job_Manage():

    @allure.title("添加岗位类别")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：添加岗位类别")
    @allure.severity("blocker")
    @pytest.mark.parametrize("name,explain", [('zdh_岗位类别名称13', 'zdh_说明13')])
    def test_add_job(self, login_cf, name, explain):
        '''
        :param login_cf: 登录
        1.添加岗位类别
        :return:
        '''
        driver = login_cf
        web = Job_Manage(driver)
        web.click_job_menu()
        text = web.add_job(name=name, explain=explain)
        assert text == "添加成功"

    @allure.title("编辑岗位类别")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：编辑岗位类别")
    @allure.severity("blocker")
    @pytest.mark.parametrize("name,explain", [('zdh_岗位类别名称08_编辑13', 'zdh_说明08_编辑13')])
    def test_edit_job(self, login_cf, name, explain):
        '''
        :param login_cf: 登录
        1.编辑岗位类别
        :return:
        '''
        driver = login_cf
        web = Job_Manage(driver)
        web.click_job_menu()
        text = web.edit_job(name=name, explain=explain)
        assert text == "修改成功"

    @allure.title("禁用启用岗位类别")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：禁用启用岗位类别")
    @allure.severity("blocker")
    def test_disabled_job(self, login_cf):
        '''
        :param login_cf: 登录
        1.禁用启用岗位类别
        :return:
        '''
        driver = login_cf
        web = Job_Manage(driver)
        web.click_job_menu()
        text = web.disabled_job()
        assert text == "禁用成功" or "启用成功"

    @allure.title("岗位类别-详情")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：岗位类别-详情")
    @allure.severity("blocker")
    def test_details_job(self, login_cf):
        '''
        :param login_cf: 登录
        1.岗位类别-详情
        :return:
        '''
        driver = login_cf
        web = Job_Manage(driver)
        web.click_job_menu()
        text = web.details_job()
        assert text == "岗位类别管理"

    @allure.title("岗位类别-查询")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：岗位类别-查询")
    @allure.severity("blocker")
    @pytest.mark.parametrize("name", ["交通工程质监"])
    def test_details_job(self, login_cf, name):
        '''
        :param login_cf: 登录
        1.岗位类别-查询
        :return:
        '''
        driver = login_cf
        web = Job_Manage(driver)
        web.click_job_menu()
        text = web.search_job(name=name)
        assert text == name


