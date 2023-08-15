import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GetDriver:
    # 1.声明变量
    __web_driver=None

    # 2.获取driver方法
    # 修饰符对应的函数不需要实例化, 不需要self参数,
    # 方便调用，不用实例化
    # 但第一个参数需要是表示自身类的cls参数, 可以来调用类的属性, 类的方法, 实例化对象等
    @classmethod
    def get_web_driver(cls,url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 去掉自动化标识
            option = Options()
            option.add_experimental_option('excludeSwitches', ['enable-automation'])
            option.add_argument('--disable-blink-features=AutomationControlled')
            # 屏蔽'保存密码'提示框
            prefs = {}
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            option.add_experimental_option("prefs", prefs)
            # 获取浏览器
            cls.__web_driver=webdriver.Chrome(options=option)
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)

        # 返回driver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None

