from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
import scripts


class TestSellerLogin:
    # 初始化
    def setup_class(self):
        # 调用driver
        driver = GetDriver.get_web_driver(page.url_seller)
        # 通过统一入口类获取PageSellerLogin对象
        self.seller = PageIn(driver).page_get_PageSellerLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test_seller_login(self, username=scripts.seller_username, code=scripts.seller_code,expect=scripts.seller_expect):
        # 调用登录业务方法
        self.seller.page_seller_login(username, code)
        try:
            # 断言
            assert expect == self.seller.page_get_info()
        except Exception as e:
            # 截图
            self.seller.base_get_img()
            # 抛异常
            raise
