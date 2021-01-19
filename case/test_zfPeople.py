import pytest
import allure
from pages.zfPeople_page import ZF_People

@allure.epic("行政执法项目")
@allure.feature("执法人员管理")
@pytest.mark.ui_select
class Test_zfPeople():

    @allure.title("添加执法人员")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：添加执法人员")
    @allure.severity("blocker")
    def test_add_zf_people(self, login_cf):
        '''
        :param login_cf: 登录
        1.添加执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        text = web.add_zf_people()
        assert text == "添加成功"
        web.get_img()

    def test_search_zf_people(self, login_cf):
        '''
        :param login_cf: 登录
        1.查询执法人员
        :return:
        '''
        driver = login_cf
        web = ZF_People(driver)
        web.click_zf_menu()
        text = web.search_fz_people()
        assert text == "陈凯"
        web.get_img()
