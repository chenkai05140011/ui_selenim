import pytest
import allure
from pages.tag import Org_Entity

@allure.epic("行政执法项目")
@allure.feature("打标签")
class Test_Tag():

    @allure.title("机构类打标签")
    @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    @allure.description("case描述：新增tag")
    @allure.severity("blocker")
    def test_add_org_tag(self, login_cf):
        '''
        :param login_cf: 登录
        1.新增tag
        :return:
        '''
        driver = login_cf
        web = Org_Entity(driver)
        web.click_tag()
        text = web.add_tag()
        assert text == "标签添加成功"





