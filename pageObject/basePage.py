import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from common.logger import Logger
from common.readFile import ReadFile

logger = Logger()

class BasePage():
    "定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类"

    def __init__(self, driver):
        self.driver = driver
        config = ReadFile()
        self.baseurl = config.readConfig("BaseUrl", "url")

    def open_url(self, url):
        self.driver.get(self.baseurl + url)

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 查找元素
    def find_element(self, selector):
        selector_by = selector['find_type']
        selector_value = selector['element_info']

        try:
            if selector_by == 'id':
                el = self.driver.find_element_by_id(selector_value)
            elif selector_by == "n" or selector_by == 'name':
                el = self.driver.find_element_by_name(selector_value)
            elif selector_by == 'cs' or selector_by == 'css_selector':
                el = self.driver.find_element_by_css_selector(selector_value)
            elif selector_by == 'cn' or selector_by == 'classname':
                el = self.driver.find_element_by_class_name(selector_value)
            elif selector_by == "lt" or selector_by == 'link_text':
                el = self.driver.find_element_by_link_text(selector_value)
            elif selector_by == "plt" or selector_by == 'partial_link_text':
                el = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by == "tn" or selector_by == 'tag_name':
                el = self.driver.find_element_by_tag_name(selector_value)
            elif selector_by == "x" or selector_by == 'xpath':
                el = self.driver.find_element_by_xpath(selector_value)
            elif selector_by == "ss" or selector_by == 'selector_selector':
                el = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError("Please enter a valid type of targeting elements.")
        except NoSuchElementException  :
            logger.error("{0}页面中未能找到{1}元素".format(self, selector_value))

        return el

    # 输入
    def input(self, selector, text):
        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        try:
            logger.info("The element \' %s \' was clicked." % el.text)
            el.click()
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    def get_text(self,selector):
        el = self.find_element(selector)
        try:
            return el.text
        except NameError as e:
            logger.error("Failed to text the element with %s" % e)

    def switch_frame(self, selector):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            el = self.find_element(selector)
            return self.driver.switch_to_frame(el)
        except NoSuchElementException as e:
            logger.error("查找iframe异常-> {0}".format(e))

    def switch_windows(self, selector):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            el = self.find_element(selector)
            return self.driver.switch_to_window(el)
        except NoSuchElementException as e:
            logger.error("查找窗口句柄handle异常-> {0}".format(e))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoSuchElementException as e:
            logger.error("查找alert弹出框异常-> {0}".format(e))

if __name__ == '__main__':
    bg = BasePage(webdriver.Chrome())
    bg.open_url('/login')



