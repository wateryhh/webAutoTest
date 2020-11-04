import unittest
from  common.function import latest_report
from  common.sendMail import *
from config import setting
from thridLib.HTMLTestRunner import HTMLTestRunner
import time
import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
report_dir = setting.TEST_REPORT + '/report/'

def add_case(test_path=setting.TEST_DIR):
    discover = unittest.defaultTestLoader.discover(test_path, pattern="test*.py")
    return discover

def run_case(all_case,result_path=report_dir):
    print("start run testcase...")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = result_path + '/' + now + 'result.html'
    print("start write report...")

    #HTMLTestRunner测试报告
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况')  # 定义测试报告
        runner.run(all_case)  # 执行测试用例
    f.close()

    print("find latest report...")
    # 查找最新的测试报告
    report = latest_report(result_path)
    # 邮件发送报告
    print("send email report...")
    send_mail(report)
    print("test end!")

if __name__ == '__main__':
    cases = add_case()
    run_case(cases)