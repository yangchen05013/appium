#!/usr/bin/env python
#coding=utf-8
import VideoPage
import unittest

class Test_web(unittest.TestCase):



    def test_login(self):
        VideoPage.test_login(self)

    def test_login_wechat(self):
        VideoPage.test_login_wechat(self)


    def test_login_qq(self):
        VideoPage.test_login_qq(self)

    def test_socialdiscuss_publishtopic(self):
        VideoPage.test_socialdiscuss_publishtopic(self)

    def test_socialdiscuss_refreshlist(self):
        VideoPage.test_socialdiscuss_refreshlist(self)

    def test_socialdiscuss_loadlist(self):
        VideoPage.test_socialdiscuss_loadlist(self)

    def test_social_refresh(self):
        VideoPage.test_social_refresh(self)

    def test_social_deletemyitem(self):
        VideoPage.test_social_deletemyitem(self)


