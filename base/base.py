import base64
import allure
import cv2
from selenium.webdriver.support.wait import WebDriverWait

"""page页面基类，page页面公共方法目录"""


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc:格式为列表或元组，内容：元素定位信息使用By类
        :param timeout:查找元素超时时间，默认30s
        :param poll:查找元素的频率，默认为0.5s
        :return:元素
        """
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 1.获取元素
        ele = self.base_find(loc)
        # 2.清空操作
        ele.clear()
        # 3.输入操作
        ele.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc:元素定位信息
        """
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取滑块图片
    def base_get_pic(self, loc1, loc2, big_pic, small_pic):
        """
        :param loc1: 滑块背景图定位信息
        :param loc2: 滑块缺块图定位信息
        :param big_pic: 滑块背景图
        :param small_pic: 滑块缺块图
        """
        big_ele = self.base_find(loc1)
        small_ele = self.base_find(loc2)
        # 获取属性
        big_src = big_ele.get_attribute('src')
        small_src = small_ele.get_attribute('src')
        # print(small_src)
        # 获取标准base64编码
        big_src = big_src[big_src.find(',') + 1:]
        small_src = small_src[small_src.find(',') + 1:]
        # 写入文件（写二进制）
        with open(big_pic, mode='wb') as f:
            # 先把base64转成二进制，然后写入文件
            f.write(base64.b64decode(big_src))

        with open(small_pic, mode='wb') as f:
            # 先把base64转成二进制，然后写入文件
            f.write(base64.b64decode(small_src))

    # 验证码破解
    def base_findloc(self, target, template):
        """
        找出图像中最佳匹配位置
        :param target: 目标及背景图
        :param template: 模块即需要找到的图
        :return: 返回最佳匹配及其最差匹配和对应的坐标
        """
        target_rgb = cv2.imread(target)
        target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
        template_rgb = cv2.imread(template, 0)
        res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
        value = cv2.minMaxLoc(res)
        print(value)
        # 返回最佳匹配的X坐标
        return value[2][0]

    # 获取 方法封装
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回文本值
        """
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用 将图片写入报告方法
        self.__base_write_image()

    # 图片写入allure报告方法（私有化）
    def __base_write_image(self):
        # 获取图片流
        with open("./image/err.png", "rb") as f:
            # 调用 allure.attach方法将图片写入报告
            allure.attach(f.read(),"失败原因：", allure.attachment_type.PNG)