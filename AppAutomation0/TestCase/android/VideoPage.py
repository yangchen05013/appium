#coding=utf-8
#!/usr/bin/env python
import time

from selenium.common.exceptions import NoSuchElementException

from TestCase.AndroidAppTest import *
from TestPage.android.mainpagelocator import *


def test_add_contacts(self):
    try:
        driver=AndroidAppTestBase.setUpClass()
        time.sleep(5)
        # #点击视频页面
        driver.find_element_by_android_uiautomator(newproject).click()
        driver.find_element_by_android_uiautomator(btncancel).click()
    except NoSuchElementException, e:
        raise e
    finally:
        AndroidAppTestBase.tearDownClass()

def test_add_contacts1(self):
    try:
        driver=AndroidAppTestBase.setUpClass()
        time.sleep(5)
        # #点击视频页面
        driver.find_element_by_android_uiautomator(newproject).click()
        driver.find_element_by_android_uiautomator(btncancel).click()
    except NoSuchElementException, e:
        raise e
    finally:
        AndroidAppTestBase.tearDownClass()

def Videopageinfo(self):
    try:
        driver=AndroidAppTestBase.setUpClass()
        time.sleep(5)
        # #点击视频页面
        driver.find_element_by_android_uiautomator(newproject).click()
        driver.find_element_by_android_uiautomator(btncancel).click()
    except NoSuchElementException, e:
        raise e
    finally:
         driver.quit()


