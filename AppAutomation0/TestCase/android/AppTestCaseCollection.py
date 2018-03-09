#!/usr/bin/env python
#coding=utf-8
from appium import webdriver
from TestCase.AndroidAppTest import *
import VideoPage
import unittest

class Test_web(unittest.TestCase):

    def test_add_contacts(self):
        VideoPage.test_add_contacts(self)

    def test_add_contacts1(self):
        VideoPage.test_add_contacts1(self)
        
    def Videopageinfo(self):
        """


        """
        VideoPage.Videopageinfo(self)