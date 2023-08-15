import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import scripts

class TestSellerPublish:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_seller)
        # 2. 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3. 获取PageSellerLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageSellerLogin().page_seller_login_ok()
        # 4. 获取PageSellerPublish页面对象
        self.publish = self.page_in.page_get_PagePublish()

    # 2. 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3. 测试发布商品方法
    def test_publish(self, name=scripts.publish_name):
        # 调用发布文章业务方法
        self.publish.page_publish(name)
        # 查看断言信息
        print("发布商品结果为：", self.publish.page_get_info())