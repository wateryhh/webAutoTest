import time
from selenium import webdriver

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config import setting

def inser_img(driver):
    # 指定截图存放的根目录路径
    screen_dir = setting.TEST_REPORT + '/imges/'
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_name = screen_dir + rq + '.png'
    driver.get_screenshot_as_file(screen_name)
    print('screenshot:' + screen_name)

#查找最新的测试报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    file = os.path.join(report_dir, lists[-1])
    return file

def latest_report_img(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    file = os.path.join(report_dir, lists[-1])
    return file

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.get('http://www.baidu.com')
    inser_img(dr)