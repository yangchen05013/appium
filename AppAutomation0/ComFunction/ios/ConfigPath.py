#!/usr/bin/env python
#coding=utf-8

import  os
path=os.getcwd()
parent_path = os.path.dirname(os.path.dirname(path))

#发生错误截屏图片存放地址
Screenshotaddress=parent_path+"\\SnapShot\\Exceptionshot\\"

#页面操作截屏图片存放地址ַ
Pageshotaddress=parent_path+"\\SnapShot\\ActivePageshot\\"

#语言包地址
Languageadress=parent_path+"\\Languagepackage"

#升级文件地址路径
Upgradefileaddress=parent_path+"\\plug\\plugins"

#报告生成路径
Run_Report_andorid=parent_path+"\\Run_Report\\android"

#报告生成路径
Run_Report_ios=parent_path+"\\Run_Report\\ios"

#页面操作截屏图片存放地址
ExpectImageshotaddress=parent_path+"\\SnapShot\\ExpertpageShot\\"