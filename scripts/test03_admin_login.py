from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
import scripts

class TestAdminLogin:
    # 初始化
    def setup_class(self):
        # 调用driver
        driver = GetDriver.get_web_driver(page.url_manager)
        # 通过统一入口类获取PageSellerLogin对象
        self.admin = PageIn(driver).page_get_PageAdminLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test_admin_login(self, username=scripts.admin_username, code=scripts.admin_code,expect=scripts.admin_expect):
        # 调用登录业务方法
        self.admin.page_admin_login(username, code)
        try:
            # 断言
            assert expect == self.admin.page_get_info()
        except Exception as e:
            # 截图
            self.admin.base_get_img()
            # 抛异常
            raise

