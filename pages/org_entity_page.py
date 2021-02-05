from common.base_page import BasePage

class Org_Entity(BasePage):
    # 登入
    loc_menu = ("css", "span[title='监管智库']")
    loc_menu_supervision = ("css", "span[title='监管对象']")
    loc_menu_supervision_org = ("css", "span[title='机构类主体']")
# 缺少自动标签部分

    def menu_org(self):
        self.click(self.loc_menu)
        self.click(self.loc_menu_supervision)
        self.click(self.loc_menu_supervision_org)
        self.sleep(5)



    def search_org(self):
        pass

    loc_add_org_button = ("css", ".operate .ant-btn-primary")
    loc_add_org_name = ("css", ".ant-modal-content [formcontrolname=orgEntityName]")
    loc_add_org_status = ("css", "[formcontrolname=avaliable]")
    loc_add_org_status_all = ("css", "[role=menu] li:nth-child(1)")
    loc_add_org_status_n = ("css", "[role=menu] li:nth-child(2)")
    loc_add_org_status_y = ("css", "[role=menu] li:nth-child(3)")
    loc_add_org_search = ("css", ".ant-modal-body .search-area .ant-btn-primary")
    loc_tick = ("css", ".ant-modal-body [type='checkbox']")
    loc_add_org_manage_button = ("css", ".ant-modal-body>div button")
    loc_alert = ("css", ".ant-message span")
    def add_org(self, name='台州市跃驰汽配有限公司'):
        self.click(self.loc_add_org_button)
        self.type(self.loc_add_org_name, name)
        self.click(self.loc_add_org_status)
        self.click(self.loc_add_org_status_y)
        self.click(self.loc_add_org_search)
        self.click(self.loc_tick)
        self.click(self.loc_add_org_manage_button)
        self.get_img()
        text = self.get_text(self.loc_alert)
        return text


    def manage_org(self):
        pass

    def batch_add_tag_org(self):
        pass

    def batch_del_manage(self):
        pass

    def batch_del_tag(self):
        pass


