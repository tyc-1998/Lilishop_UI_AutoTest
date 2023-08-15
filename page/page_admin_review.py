from base.base import Base
import page
from time import sleep


class PageAdminReview(Base):
    # 点击 待审核商品模块
    def page_click_model(self):
        sleep(1)
        self.base_click(page.product)

    # 填写商品名称,并搜索
    def page_name_search(self,name):
        sleep(1)
        self.base_click(page.product_name)
        self.base_input(page.product_name,name)
        sleep(1)
        self.base_click(page.admin_search_btn)

    # 审核商品
    def page_review_goods(self):
        sleep(1)
        self.base_click(page.pass_btn)
        sleep(1)
        self.base_click(page.sure_btn)

    # 查看商品上架是否成功
    def page_pass_success(self,name):
        sleep(1)
        self.base_click(page.platform_btn)
        self.base_input(page.product_name, name)
        sleep(1)
        self.base_click(page.admin_search_btn)
        return self.base_get_text(page.review_res)

    # 组合审核商品业务方法
    def page_review(self, name):
        self.page_click_model()
        sleep(1)
        self.page_name_search(name)
        sleep(1)
        self.page_review_goods()

