# coding=utf-8
import time
import unittest

from appium import webdriver

# define APPCenter test class


class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            # 此处填写机器的android版本
            'platformVersion': '7.0',
            # 填写adb devices -l 中显示的第一列的设备号
            'deviceName': '9e0f5e4d',
            'appPackage': 'com.huawei.appmarket',
            'appActivity': '.MainActivity',
            'appWaitActivity': '.MarketActivity',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
#
    def test_simple(self):
        el1 = self.driver.find_element_by_id(
            'com.huawei.appmarket:id/tab_name')
        el1.click()
        time.sleep(2)
        print 'abc'

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
