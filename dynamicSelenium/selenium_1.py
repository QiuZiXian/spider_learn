# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/14  19:33
# @abstract    :  有问题f

from selenium import webdriver
# print(help(webdriver)) # 查看支持的浏览器
url = "http://www.kuman.com/mh-1002960/"

browser = webdriver.PhantomJS()
browser.implicitly_wait(10)

browser.get(url)
print(browser.title)
browser.save_screenshot('doupo.png')
# browser.set_window_size(400, 300)
src = browser.find_element_by_css_selector("#wdwailian img").get_attribute("src")
div = browser.find_element_by_id("wdwailian")
print(src, "/n", div)

browser.close()