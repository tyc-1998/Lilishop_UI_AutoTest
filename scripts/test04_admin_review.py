import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import scripts

class TestAdminReview:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_manager)
        # 2. 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3. 获取PageAdminLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageAdminLogin().page_admin_login_ok()
        # 4. 获取PageReview页面对象
        self.review = self.page_in.page_get_PageReview()

    # 2. 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3. 测试审核商品方法
    def test_review(self, name=scripts.publish_name):
        # 调用发布文章业务方法
        self.review.page_review(name)
        # 查看断言信息
        print("发布商品结果为：", self.review.page_pass_success(name))