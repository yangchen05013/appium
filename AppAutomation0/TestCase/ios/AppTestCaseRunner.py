#!/usr/bin/env python
#coding=utf-8
import os
import time
import unittest
import smtplib

import AppTestCaseCollection
import ComFunction.ios.ConfigPath
from ComFunction import HTMLTestRunner
ISOTIMEFORMAT='%Y%m%d%H%M%S'
from email.mime.text import MIMEText

#创建测试套件
testsuite = unittest.TestSuite()

##testsuite.addTest(AppTestCaseCollection.Test_web("test_login"))
##testsuite.addTest(AppTestCaseCollection.Test_web("test_social_refresh"))
#testsuite.addTest(AppTestCaseCollection.Test_web("test_login_wechat"))
#testsuite.addTest(AppTestCaseCollection.Test_web("test_login_qq"))
testsuite.addTest(AppTestCaseCollection.Test_web("test_socialdiscuss_publishtopic"))
##testsuite.addTest(AppTestCaseCollection.Test_web("test_socialdiscuss_refreshlist"))
##testsuite.addTest(AppTestCaseCollection.Test_web("test_socialdiscuss_loadlist"))
##testsuite.addTest(AppTestCaseCollection.Test_web("test_social_deletemyitem"))




filename = 'E:/AppAutomation0/Run_Report/ios/'+str(time.strftime(ISOTIMEFORMAT)) + "iOS.html"
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'您好！以下是准入测试结果',
    description=u'千山降压准入测试结果'
)
runner.run(testsuite)



#定义发送邮件
def sentmail(file_new):

    #发信邮箱
    mail_from = 'yangzhijun@chinasunhealth.com'
    # 收信邮箱
    mail_to = ['402642554@qq.com','21113890@qq.com']
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #定义标题
    msg['Subject'] = u"千山降压测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    #连接SMTP服务器，此处用163的SMTP服务器
    smtp.connect('smtp.exmail.qq.com')
    smtp = smtplib.SMTP('smtp.exmail.qq.com',25)
    # #用户名密码
    smtp.login('yangzhijun@chinasunhealth.com', 'K198803012e')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out !'
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'F:\\AppAutomation0\\Run_Report\\ios'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'最新测试生成的报告: ' + lists[-2])
    #找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-2])
    print file_new
    #调用发邮件模块
    sentmail(file_new)
sendreport()