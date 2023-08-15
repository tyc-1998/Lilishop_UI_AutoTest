from selenium.webdriver.common.by import By

"""以下数据为卖家，后台管理url"""
# 卖家url
url_seller = "https://store-b2b2c.pickmall.cn"
# 后台管理url
url_manager = "https://admin-b2b2c.pickmall.cn"

"""以下数据为卖家发布商品模块配置数据 元素定位信息"""
# 用户名
seller_username = (By.CSS_SELECTOR, "[placeholder='请输入用户名']")
# 密码
seller_code = (By.CSS_SELECTOR, "[placeholder='请输入密码']")
# 登录按钮
seller_login_btn = (By.CSS_SELECTOR, ".login-btn")
# 滑块
seller_big_loc = (By.XPATH, '//*[@id="main"]/div/div/div/div[4]/div[1]/img[1]')
seller_small_loc = (By.CSS_SELECTOR, ".slider")
seller_slide = (By.CSS_SELECTOR, ".swiper")
# 滑块背景图
seller_big_pic = "./image/seller_big.png"
# 缺块图
seller_small_pic = "./image/seller_small.png"
# 登录成功
login_ok = (By.XPATH,"//*[contains(text(),'店铺名称：Apple官方自营旗舰店')]")

# 商品模板
seller_model = (By.XPATH, "//*[contains(text(),' 商品模板 ')]")
# 商品编号框
goods = (By.CSS_SELECTOR, "[placeholder='商品编号']")
# 商品编号
numbers = '1672071747204218882'
# 搜索
search_btn = (By.XPATH, "//*[contains(text(),'搜索')]")
# 编辑
edit_btn = (By.XPATH, "//span[text()='编辑']/..")
# 商品名称
goods_name = (By.CSS_SELECTOR, "[placeholder='商品名称']")
# 保存商品
save_btn = (By.XPATH, "//span[text()=' 保存商品 ']/..")
# 结果
result = (By.XPATH,"//*[contains(text(),'恭喜您，商品发布成功!')]")

"""以下数据为后台管理商品模块配置数据 元素定位信息"""
# 用户名
admin_username = (By.CSS_SELECTOR, "[placeholder='请输入用户名']")
# 密码
admin_code = (By.CSS_SELECTOR, "[placeholder='请输入密码']")
# 登录
admin_login_btn = (By.CSS_SELECTOR, ".login-btn")
# 滑块
admin_big_loc = (By.XPATH, '//*[@id="main"]/div/div/div/div[3]/div[1]/img[1]')
admin_small_loc = (By.CSS_SELECTOR, ".slider")
admin_slide = (By.CSS_SELECTOR, ".swiper")
# 滑块背景图
admin_big_pic = "./image/admin_big.png"
# 缺块图
admin_small_pic = "./image/admin_small.png"
# 登录成功
admin_login_ok = (By.XPATH,"//*[contains(text(),'RageEX')]")

# 待审核商品
product = (By.XPATH, "//*[contains(text(),'待审核商品')]")
# 输入商品名称
product_name = (By.CSS_SELECTOR, "[placeholder='请输入商品名称']")
# 搜索
admin_search_btn = (By.XPATH, "//*[contains(text(),'搜索')]")
# 暂无数据
no_product = (By.XPATH, "//*[contains(text(),'暂无数据')]")
# 审核通过
pass_btn = (By.XPATH, '//*[@id="main"]/div/div[3]/div/div/div/div/div[1]/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/div/button[1]/span')
# 确认审核
sure_btn = (By.XPATH, "//span[text()='确定']/..")
# 平台商品
platform_btn = (By.XPATH, "//*[contains(text(),' 平台商品 ')]")
# 审核状态
review_res = (By.XPATH,'//*[@id="main"]/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[7]/div/div/span')