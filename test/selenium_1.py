# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/14  19:33
# @abstract    :  有问题f

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
# print(help(webdriver)) # 查看支持的浏览器
url = "http://www.kuman.com/mh-1002960/"

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["pthantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER")
# browser = webdriver.PhantomJS()
browser = webdriver.Firefox()
browser.implicitly_wait(10)
url = "http://www.bimclub.cn/down/201711/03/1273.html"
browser.get(url)
btn =browser.find_element_by_class_name("t")
btn.click()
browser.quit()

# browser.get(url)
# print(browser.title)
# browser.save_screenshot('doupo.png')
# # browser.set_window_size(400, 300)
# src = browser.find_element_by_css_selector("#wdwailian img").get_attribute("src")
# div = browser.find_element_by_id("wdwailian")
# print(src, "/n", div)
#
# browser.close()