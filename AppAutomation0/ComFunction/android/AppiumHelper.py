#coding=utf-8
#!/usr/bin/env python
#通过ID获取页面元素
from appium import webdriver
#点击页面元素方法
def click(self,element):
    self.driver.find_element_by_android_uiautomator(element).click()
    # webdriver.WebElement.find_element_by_android_uiautomator(self,element).click()
#输入值方法
def send_keys(self,element, keys):
    self.driver.find_element_by_android_uiautomator(element).send_keys(keys)


#用一个滑动手势进行下拉刷新
def tap(self):
    js_snippet = "mobile: swipe"
    args = {'startX':0.5, 'startY':0.2, 'startX':0.5, 'startY':0.95, 'tapCount':1, 'duration':10}
    self.driver.execute_script(js_snippet, args)


def screenshot(self,filename):
    self.driver.get_screenshot_as_file(filename)

