import pytest
import allure
from pages.zfPeople_page import ZF_People

@allure.epic("行政执法项目")
@allure.feature("执法人员库")
@pytest.mark.ui_test
class Test_zfPeople():

    @allure.title("添加执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：添加执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("phone", ['13186977800', '15925990921'])
    def test_add_zf_people(self, login_cf, phone):
        '''
        :param login_cf: 登录
        1.添加执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        text = web.add_zf_people(phone=phone)
        assert text == "添加成功"

    @allure.title("查询执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：查询执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("name", ["陈凯"])
    def test_search_zf_people(self, login_cf, name):
        '''
        :param login_cf: 登录
        1.查询执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        text = web.search_fz_people(name=name)
        assert text == name

    @allure.title("编辑执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：编辑执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("phone", ['13186977800', '15925990921'])
    def test_edit_zf_people(self, login_cf, phone):
        '''
        :param login_cf: 登录
        1.编辑执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        text = web.edit_fz_people(phone=phone)
        assert text == "修改成功"

    @allure.title("禁用启用执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：禁用启用执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("phone", ['13186977800', '15925990921'])
    def test_disabled_zf_people(self, login_cf,phone):
        '''
        :param login_cf: 登录
        1.禁用启用执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        web.disabled_fz_people(phone=phone)

    @allure.title("详情执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：添加执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("phone", ['13186977800', '15925990921'])
    def test_details_zf_people(self, login_cf, phone):
        '''
        :param login_cf: 登录
        1.详情执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        web.details_fz_people(phone=phone)


    @allure.title("删除执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：删除执法人员")
    @allure.severity("blocker")
    @pytest.mark.parametrize("phone", ['13186977800', '15925990921'])
    def test_del_zf_people(self, login_cf, phone):
        '''
        :param login_cf: 登录
        1.删除执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        web.del_fz_people(phone=phone)