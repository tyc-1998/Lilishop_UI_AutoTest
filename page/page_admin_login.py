from time import sleep
from selenium.webdriver import ActionChains
from base.base import Base
import page


class PageAdminLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中的输入方法
        self.base_input(page.admin_username, username)

    # 输入密码
    def page_input_code(self, code):
        self.base_input(page.admin_code, code)

    # 点击登录按钮
    def page_click_login(self):
        sleep(1)
        self.base_click(page.admin_login_btn)

    # 滑块验证
    def page_slide(self):
        url = self.driver.current_url
        while True:
            if self.driver.current_url != url:
                break
            self.base_get_pic(page.admin_big_loc, page.admin_small_loc,page.admin_big_pic,page.admin_small_pic)
            res = self.base_findloc(page.admin_big_pic, page.admin_small_pic)
            print(res)
            slide_ele = self.base_find(page.admin_slide)
            action = ActionChains(self.driver)
            action.click_and_hold(slide_ele).move_by_offset(res, 0).release().perform()
            sleep(1)

    # 获取昵称框信息封装----测试脚本断言使用
    def page_get_info(self):
        return self.base_get_text(page.admin_login_ok)

    # 组合业务方法-----测试脚本层调用
    def page_admin_login(self, username, code):
        """调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login()
        self.page_slide()

    # 组合业务方法-----审核商品依赖使用
    def page_admin_login_ok(self, username="admin", code="123456"):
        """调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login()
        self.page_slide()