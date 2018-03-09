#coding=utf-8

from appium import webdriver
import os
import time
import unittest


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppTestBase(unittest.TestCase):
    def test_find_elements(self):
        time.sleep(5)
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()
        time.sleep(2)
        el = self.driver.find_element_by_accessibility_id('Arcs')
        self.assertIsNotNone(el)
        self.driver.back()
        time.sleep(2)
        el = self.driver.find_element_by_accessibility_id("App")
        self.assertIsNotNone(el)
        time.sleep(2)
        els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        self.assertGreaterEqual(12, len(els))
        self.driver.find_element_by_android_uiautomator('text("API Demos")')


    def test_simple_actions(self):
        time.sleep(2)
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()
        time.sleep(2)
        el = self.driver.find_element_by_accessibility_id('Arcs')
        el.click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')


    def getDriver(self,sAppiumIP,sPort,sMobOS,Version,appPath,DeviceName):
        remoteUrl = str.format("http://%s:%s/wd/hub", sAppiumIP, sPort);
        MobOSStr = sMobOS.toUpperCase().trim();
        if(MobOSStr=="ANDROID"):
            # desired_caps = {}
            # desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = Version #'4.4'
            # desired_caps['deviceName'] =DeviceName
            # desired_caps['app'] = appPath #PATH('D:\AutomationTest\AutomationRunner\Installer\Android\FilmoraGo-release.apk')
            # desired_caps['appPackage'] = 'com.wondershare.filmorago'
            # desired_caps['appActivity'] = 'com.wondershare.filmorago.activity.WelcomeActivity'
            #
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '4.4'
            desired_caps['deviceName'] = '192.168.24.2:5554'
            desired_caps['appPackage'] = 'com.wondershare.filmorago'
            desired_caps['appActivity'] = 'com.wondershare.filmorago.activity.WelcomeActivity'
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        elif(MobOSStr=="IOS"):
            desired_caps = {}
            desired_caps['platformName'] = 'iOS'
            desired_caps['platformVersion'] = Version #'7.0'
            desired_caps['deviceName'] =DeviceName # 'iPhone 4S'
            desired_caps['UDID'] = '85f55bfdaaf6a96662f0d0ecbcd7882df8e96b88'
            desired_caps['app'] =appPath #PATH('D:\AutomationTest\AutomationRunner\Installer\iOS\test.app')
        self.driver = webdriver.Remote(remoteUrl, desired_caps)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTestBase)
    unittest.TextTestRunner(verbosity=2).run(suite)
