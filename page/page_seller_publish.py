from base.base import Base
import page
from time import sleep


class PageSellerPublish(Base):
    # 点击 商品模块
    def page_click_model(self):
        sleep(1)
        self.base_click(page.seller_model)

    # 填写商品编号,并搜索
    def page_num_search(self):
        sleep(1)
        self.base_click(page.goods)
        self.base_input(page.goods,page.numbers)
        sleep(1)
        self.base_click(page.search_btn)
        sleep(1)
        self.base_click(page.edit_btn)

    # 编辑，保存商品
    def page_save_goods(self,name):
        sleep(1)
        self.base_click(page.goods_name)
        self.base_input(page.goods_name,name)
        self.base_click(page.save_btn)

    # 获取 发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.result)

    # 组合发布商品业务方法
    def page_publish(self, name):
        self.page_click_model()
        self.page_num_search()
        self.page_save_goods(name)

