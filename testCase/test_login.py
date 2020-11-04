import unittest
from common import function,myUnit,readFile
from pageObject.loginPage import CndsPage
from time import sleep
from common.logger import Logger
from config import setting
import ddt

log = Logger()

testData= readFile.ReadFile().readYaml(setting.TEST_DATA_YAML + '/' + 'login_data.yaml')

@ddt.ddt
class LoginTest(myUnit.StartEnd):
    # @unittest.skip('skip this case')
    """CNDS登录测试"""
    def user_login_verify(self,account,passwd):
        """
        用户登录
        :param :account 账号
        :param passwd: 密码
        :return:
        """
        CndsPage(self.driver).accout_login(account,passwd)

    @ddt.data(*testData)
    def test_login_normal(self,datayaml):
        log.info("test_login1_normal is start run...")
        self.user_login_verify(datayaml['data']['accout'],datayaml['data']['passwd'])
        sleep(3)
        #断言与截屏
        po = CndsPage(self.driver)
        if datayaml['screenshot'] == 'login_success':
            po.get_account()
            function.inser_img(self.driver)
            self.assertEqual(po.user_login_success(), datayaml['check'][0], "登录成功，返回实际结果是->: {0}".format(po.user_login_success()))
        else:
            function.inser_img(self.driver)
            self.assertEqual(po.accout_passwd_error(), datayaml['check'][0],"登录失败，返回实际结果是->: {0}".format(po.accout_passwd_error()))
        print("test_login1_normal is test end!")

if __name__ == '__main__':
    unittest.main()