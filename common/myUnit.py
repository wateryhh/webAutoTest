import unittest
from common.driver import Browser

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = Browser().driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    s = StartEnd()
    s.setUp()

