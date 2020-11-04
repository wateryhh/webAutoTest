from common.readFile import ReadFile
from common.logger import Logger
from selenium import webdriver

logger = Logger()

from selenium.webdriver import Remote

class Browser():

    def __init__(self):
        config = ReadFile()
        self.browser = config.readConfig("Browser", "browser")
        self.host = config.readConfig("host","host")
        logger.info("You had select {} host {} browser.".format(self.host,self.browser))

    def driver(self):
        """
        启动浏览器驱动
        :return: 返回浏览器驱动URL
        """
        try:
            # driver = webdriver.Chrome()
            driver = Remote(command_executor='http://' + self.host + '/wd/hub',
                            desired_capabilities={ 'platform': 'ANY',
                                                   'browserName': self.browser,
                                                   'version': "",
                                                   'javascriptEnabled': True
                                                }
                            )
            return driver
        except Exception as msg:
            print("驱动异常-> {0}".format(msg))

if __name__ == '__main__':
    br = Browser().driver()
    br.get('http://www.baidu.com')
