#-*- coding: utf-8 -*-

from appium import webdriver
import os
import unittest
import time

import urllib2
urllib2.getproxies = lambda: {}

# Returns abs path relative to this file and not cwd 
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)) 


class ContactsAndroidTests(unittest.TestCase): 
    def setUp(self): 
#         pass

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.1.104:5554'
        
#         desired_caps['app'] = PATH('G:\Appuim\com.example.android.contactmanager.apk')
        
#         desired_caps['appPackage'] = 'com.ipc.newipc'     # ipc not work
#         desired_caps['appActivity'] = '.GuideActivity'
#         desired_caps['appActivity'] = '.IpcMain'

#         desired_caps['appPackage'] = 'com.android.settings'     # 设置
#         desired_caps['appActivity'] = '.Settings'

        desired_caps['appPackage'] = 'com.ipc.newipc'     # ipc
        desired_caps['appActivity'] = '.LoadActivity'

#         desired_caps['appPackage'] = 'com.hummingbird.zhaoqin.kkk5'     # kkk
#         desired_caps['appActivity'] = '.MainActivity'
        
#         desired_caps['appPackage'] = 'com.ztgame.ztmobiletest'     # zt
#         desired_caps['appActivity'] = 'com.metek.mobilezt.S2Pro'

#         desired_caps['appPackage'] = 'com.android.browser'     # browser not work
#         desired_caps['appActivity'] = '.BrowserActivity'

#         desired_caps['appPackage'] = 'ty.com.android.notes'     # txt
#         desired_caps['appActivity'] = '.NotesList'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) 

    
    def tearDown(self): 
        pass
#         self.driver.quit()

    def test_add_contacts(self): 
        time.sleep(5)
        
        el=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.ipc.newipc:id/radio_button3")')
        el.click()

#         self.driver.swipe(50, 800, 50, 800, 100)    # 模拟点击动作
#         time.sleep(2)
#         self.driver.swipe(150, 800, 150, 800, 100)
#         time.sleep(2)
#         self.driver.swipe(250, 800, 250, 800, 100)
#         time.sleep(2)
#         self.driver.swipe(350, 800, 350, 800, 100)
#         time.sleep(2)
#         self.driver.swipe(450, 800, 450, 800, 100)
#         time.sleep(2)

#         self.driver.open_notifications()  # 展开通知栏

#         x = self.driver.get_window_size()['width']  # 获取窗口大小
#         y = self.driver.get_window_size()['height']  # 获取窗口大小
        
#         self.driver.swipe(x/2, 20, x/2, y-40, 2000)  # 模拟拖动操作
#         time.sleep(2)

#         x0 = x/3
#         y0 = y/3
#         
#         self.driver.swipe(x0,y0, 2*x0,y0, 2000)
#         self.driver.swipe(2*x0,y0, 2*x0,2*y0, 2000)
#         self.driver.swipe(2*x0,2*y0, x0,2*y0, 2000)
#         self.driver.swipe(x0,2*y0, x0,y0, 2000)
#         self.driver.swipe(x0,y0, 1.5*x0,1.5*y0, 2000)
#         time.sleep(2)
        
#         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("menu_add")').click()    # not work
#         self.driver.find_element_by_id("ty.com.android.notes:id/menu_add").click()    # save a note
#         time.sleep(2)
#         title = self.driver.find_element_by_id("ty.com.android.notes:id/id_editor_title")
#         title.send_keys("Appium User")
#         time.sleep(2)
#         note = self.driver.find_element_by_id("ty.com.android.notes:id/note")
#         note.send_keys("Appium User 123 over!")
#         time.sleep(2)
#         self.driver.find_element_by_id("ty.com.android.notes:id/menu_save").click()
        
#         self.driver.tap([(x0,y0), (x0,2*y0), (2*x0,2*y0), (x0,2*y0), (1.5*x0,1.5*y0)], 500)    # 模拟多点触摸操作，可以1个点，最多5个点
#         time.sleep(2)
# 
#         self.driver.save_screenshot('/storage/sdcard1/123.png')

#         self.driver.back()    # 返回
#         time.sleep(2)
        
#         self.driver.swipe(418, 395, 418, 395, 3000) # 确定
#         time.sleep(10)
#         
#         self.driver.swipe(410, 275, 410, 275, 3000) # 开始
#         time.sleep(5)
#         
#         self.driver.swipe(417, 254, 417, 254, 3000) # 进入
#         time.sleep(5)
#         
#         self.driver.swipe(423, 393, 423, 393, 3000) # 开始
#         time.sleep(5)
    
#         self.driver.quit()

#         el = self.driver.find_element_by_name("Add Contact")    # example
#         el.click() 
#         textfields = self.driver.find_elements_by_class_name("android.widget.EditText") 
#         textfields[0].send_keys("Appium User") 
#         textfields[2].send_keys("someone@appium.io") 
#         self.assertEqual('Appium User', textfields[0].text) 
#         self.assertEqual('someone@appium.io', textfields[2].text) 
#         self.driver.find_element_by_name("Save").click() 
#         # for some reason "save" breaks things 
#         alert = self.driver.switch_to_alert() 
#         alert.accept()
#         # no way to handle alerts in Android
#         self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click() 
#         self.driver.keyevent(3) 



if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

#     test_suite = unittest.TestSuite()
#     test_suite.addTest(ContactsAndroidTests("test_add_contacts")) 
#     test_result = test_suite(unittest.TestResult())
#     print test_result
