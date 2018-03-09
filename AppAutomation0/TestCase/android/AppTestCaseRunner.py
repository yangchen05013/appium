#!/usr/bin/env python
#coding=utf-8
import os
import time
import unittest
import AppTestCaseCollection
import ComFunction.android.ConfigPath
from ComFunction import HTMLTestRunner

testsuite = unittest.TestSuite()


testsuite.addTest(AppTestCaseCollection.Test_web("test_add_contacts"))
testsuite.addTest(AppTestCaseCollection.Test_web("test_add_contacts1"))
testsuite.addTest(AppTestCaseCollection.Test_web("Videopageinfo"))

time_now = str(time.localtime()[0])+str(time.localtime()[1])+str(time.localtime()[2])+str(time.localtime()[3])+str(time.localtime()[4])+str(time.localtime()[5])
file_dir = ComFunction.android.ConfigPath.Run_Report_andorid + '\\Android_qsjy' + time_now
os.makedirs(file_dir)
filename = ComFunction.android.ConfigPath.Run_Report_andorid + '\\Android_qsjy' + time_now + '\\Android.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'test',
            description=u'test'
            )
runner.run(testsuite)