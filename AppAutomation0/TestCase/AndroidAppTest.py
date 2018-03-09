#!/usr/bin/env python
#coding=utf-8
from appium import webdriver
import os
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class AndroidAppTestBase():
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = ''
        desired_caps['appPackage'] = 'com.chnsun.qianshanjy'
        desired_caps['appActivity'] = 'com.chnsun.qianshanjy.ui.MainActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return self.driver

    @classmethod
    def tearDownClass(self):
        self.driver.quit()