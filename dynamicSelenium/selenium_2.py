# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/14  20:19
# @abstract    : selenium入门之抓取百度查询结果

from selenium import webdriver

browser = webdriver.PhantomJS() # "D:/20160910/ruanjian/python3/Scripts/phantomjs"
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()

url = 'https://www.baidu.com'
browser.get(url)
# cookie = {'name':'foo', 'value':'bar'}
# browser.add_cookie(cookie)
# print(browser.get_cookies())
browser.implicitly_wait(10)

text = browser.find_element_by_id('kw')
text.clear()
text.send_keys("python")
button = browser.find_element_by_id('su')
button.submit()

print(browser.title)
browser.save_screenshot('text.png')
# # driver.set_window_size(1120, 550)
# results = browser.find_elements_by_class_name('t')
# # print(results)
# #result 类型# <selenium.webdriver.remote.webelement.WebElement (session="907c5620-e0cb-11e7-b36b-0f18fc5f19f0", element=":wdc:1513255057311")>
# for result in results:
# 	print("标题：{0} 超链接：{1}".format(result.text, result.find_element_by_tag_name('a').get_attribute('href')))
#
browser.close() # 关闭浏览器驱动，否则相当于打开了一个网页没有关闭