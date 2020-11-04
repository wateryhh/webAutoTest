from  pageObject.basePage import *
from selenium import webdriver
from common.readFile import ReadFile
from config import setting

login_el = ReadFile().readYaml(setting.TEST_Element_YAML + '/' + 'login.yaml')
data = ReadFile().readYaml(setting.TEST_DATA_YAML + '/' + 'login_data.yaml')

class CndsPage(BasePage):
    '''登录页面'''

    url = '/login'

    # 定位器，通过元素属性定位元素对象
    #选择账号密码登录
    chanlelogin_loc = login_el['testcase'][0]
    # 账号输入框
    username_loc = login_el['testcase'][1]
    # 密码输入框
    pwd_loc = login_el['testcase'][2]
    # 单击登录
    login_accout_loc = login_el['testcase'][3]

    def accout_login(self,accout,passwd):
        self.open_url(self.url)
        self.click(self.chanlelogin_loc)
        self.input(self.username_loc,accout)
        self.input(self.pwd_loc,passwd)
        self.click(self.login_accout_loc)

    # 定位器，通过元素属性定位检查项元素对象
    user_login_success_loc = login_el['check'][0]
    accout_id_loc = login_el['check'][1]
    accout_pawd_error_loc = login_el['check'][2]

    # 账号或密码错误提示
    def accout_passwd_error(self):
        return self.get_text(self.accout_pawd_error_loc)

    # 登录成功，跳转到个人资料页，获取用户名
    def get_account(self):
        self.click(self.user_login_success_loc)
        time.sleep(2)

    def user_login_success(self):
        return self.find_element(self.accout_id_loc).text

if __name__ == '__main__':
    dr = webdriver.Chrome()
    c = CndsPage(dr)
    c.accout_login('15013486261','You297043284.')
    time.sleep(2)



