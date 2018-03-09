#coding=utf-8
#!/usr/bin/env python
import time
from selenium.common.exceptions import NoSuchElementException
from TestCase.iosAppTest import *
from TestPage.ios.mainpagelocator import *





def test_login(self):
    try:
        wd=iOSAppTestBase.setUpClass()
        time.sleep(5)
        # #手机号登录
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("13480101572")
        #wd.find_element_by_name("(null)").click()
        #wd.find_element_by_name("验证码").click()
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys("1111")
        wd.find_element_by_name("登录").click()
        time.sleep(2)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()

def test_login_wechat(self):

    try:
         wd=iOSAppTestBase.setUpClass()
         time.sleep(5)
          # #微信登录
         wd.find_element_by_name("login wechat").click()
         #wd.context("WEBVIEW");
         #wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]").click()
         #wd.find_element_by_name("确认登录").click()
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()


def test_login_qq(self):
    try:
         wd=iOSAppTestBase.setUpClass()
         time.sleep(10)
         # #qq登录
         wd.find_element_by_name("login qq").click()
            #wd.context("WEBVIEW");
            #wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]").click()
            #wd.find_element_by_name("确认登录").click()
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()

def test_socialdiscuss_publishtopic(self):
    """

    :param self:
    :raise:
    """
    try:
        #查询topic表行数
        import MySQLdb
        conn = MySQLdb.connect(
            host = '192.168.1.114',
            port = 3306,
            user = 'root',
            passwd = 'hlw+2015mysql',
            db = 'chnsun_jy',
            charset='utf8')
        cur = conn.cursor()
        cout = cur.execute("SELECT * FROM topic")
        wd=iOSAppTestBase.setUpClass()
        time.sleep(10)
        # #讨论社区话题发表
        wd.find_element_by_name("main social").click()
        wd.find_element_by_name("讨论社区").click()
        wd.find_element_by_name("social discuss").click()
        wd.find_element_by_name("发表话题").click()
        time.sleep(5)
        wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').send_keys("test")
        time.sleep(5)
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("test-body")
        time.sleep(3)
        wd.find_element_by_name("键盘1").click()
        wd.find_element_by_name("发表").click()
        time.sleep(2)
        #再次查询topic表数据,判断数据是否存储
        import MySQLdb
        conn = MySQLdb.connect(
            host = '192.168.1.114',
            port = 3306,
            user = 'root',
            passwd = 'hlw+2015mysql',
            db = 'chnsun_jy',
            charset='utf8')
        cur = conn.cursor()
        cout1 = int(cur.execute("SELECT * FROM topic"))
        self.assertEquals(cout+1,cout1)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()


def test_social_deletemyitem(self):
    try:
        wd=iOSAppTestBase.setUpClass()
        time.sleep(10)
        # #删除我的收藏
        wd.find_element_by_name("main social").click()
        wd.find_element_by_name("讨论社区").click()
        wd.find_element_by_name("bs my item").click()
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]").click()
        #向左滑动一定像素
        wd.swipe(230, 108, 150, 108,500)
        wd.find_element_by_name("删除").click()
        wd.find_element_by_name("确定").click()
        time.sleep(2)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()

def test_socialdiscuss_refreshlist(self):
    try:
        wd=iOSAppTestBase.setUpClass()
        time.sleep(10)
        # #讨论社区话题华表
        wd.find_element_by_name("main social").click()
        wd.find_element_by_name("讨论社区").click()
        wd.find_element_by_name("social discuss").click()
        #向下滑动一定像素，并停留1s
        wd.swipe(180,180,180,350,1000)
        time.sleep(3)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()

def test_socialdiscuss_loadlist(self):
    try:
        wd=iOSAppTestBase.setUpClass()
        time.sleep(10)
        # #讨论社区话题华表
        wd.find_element_by_name("main social").click()
        wd.find_element_by_name("讨论社区").click()
        wd.find_element_by_name("social discuss").click()
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()

def test_social_refresh(self):
    try:
        wd=iOSAppTestBase.setUpClass()
        time.sleep(10)
        # #讨论社区话题华表
        wd.find_element_by_name("main social").click()
        wd.find_element_by_name("讨论社区").click()
        wd.find_element_by_name("social discuss").click()
        wd.swipe(330, 208, 100, 208,500) #切换到降压讲座
        #向下滑动一定像素，并停留1s
        wd.swipe(180,180,180,350,1000)
        time.sleep(3)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(5)
        #切换到降压100问
        wd.swipe(100, 208, 330, 208,500)
        wd.swipe(100, 208, 330, 208,500)
        #向下滑动一定像素，并停留1s
        wd.swipe(180,180,180,350,1000)
        time.sleep(3)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
        wd.swipe(200,560,200,230)
        time.sleep(0.2)
    except NoSuchElementException, e:
        raise e
    finally:
        iOSAppTestBase.tearDownClass()