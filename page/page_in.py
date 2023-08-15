from page.page_admin_login import PageAdminLogin
from page.page_admin_review import PageAdminReview
from page.page_seller_login import PageSellerLogin
from page.page_seller_publish import PageSellerPublish


class PageIn:
    def __init__(self,driver):
        self.driver=driver

    # 获取PageSellerLogin对象
    def page_get_PageSellerLogin(self):
        return PageSellerLogin(self.driver)

    # 获取PagePublish对象
    def page_get_PagePublish(self):
        return PageSellerPublish(self.driver)

    # 获取PageAdminLogin对象
    def page_get_PageAdminLogin(self):
        return PageAdminLogin(self.driver)

    # 获取PageAdminReview对象
    def page_get_PageReview(self):
        return PageAdminReview(self.driver)
