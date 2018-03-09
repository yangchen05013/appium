#!/usr/bin/env python
#coding=utf-8

from appium import webdriver

import os
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class iOSAppTestBase():
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] ='iPhone 6'
        # desired_caps['UDID'] = '85f55bfdaaf6a96662f0d0ecbcd7882df8e96b88'
        # desired_caps['app'] =PATH('D:\AutomationTest\AutomationRunner\Installer\iOS\test.app')
        self.wd = webdriver.Remote('http://10.0.0.11:4723/wd/hub', desired_caps)
        return self.wd

    @classmethod
    def tearDownClass(self):
        self.wd.quit()