from time import sleep
from selenium.webdriver import ActionChains
from base.base import Base
import page


class PageSellerLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中的输入方法
        self.base_input(page.seller_username, username)

    # 输入密码
    def page_input_code(self, code):
        self.base_input(page.seller_code, code)

    # 点击登录按钮
    def page_click_login(self):
        sleep(1)
        self.base_click(page.seller_login_btn)

    # 滑块验证
    def page_slide(self):
        url = self.driver.current_url
        while True:
            if self.driver.current_url != url:
                break
            self.base_get_pic(page.seller_big_loc, page.seller_small_loc,page.seller_big_pic,page.seller_small_pic)
            res = self.base_findloc(page.seller_big_pic, page.seller_small_pic)
            print(res)
            slide_ele = self.base_find(page.seller_slide)
            action = ActionChains(self.driver)
            action.click_and_hold(slide_ele).move_by_offset(res, 0).release().perform()
            sleep(1)

    # 获取昵称框信息封装----测试脚本断言使用
    def page_get_info(self):
        return self.base_get_text(page.login_ok)

    # 组合业务方法-----测试脚本层调用
    def page_seller_login(self, username, code):
        """调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login()
        self.page_slide()

    # 组合业务方法-----发布商品依赖使用
    def page_seller_login_ok(self, username="13011111111", code="111111"):
        """调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login()
        self.page_slide()