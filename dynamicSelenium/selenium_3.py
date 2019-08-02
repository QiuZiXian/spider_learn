# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/15  9:35
# @abstract    :

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() # "C:/Program Files/Mozilla Firefox/firefox"C:\Program Files\Mozilla Firefox
driver.get("http://www.python.org")
assert "Python" in driver.title # 有什么用??确定python在网页源码的title中，即没有打开错网页
driver.implicitly_wait(3)
elem = driver.find_element_by_id("id-search-field")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
driver.save_screenshot("text_3.png")
# assert "No results found" not in driver.page_source
# butn = driver.find_element_by_id("submit")  # 这边为啥不行？？？
# butn.submit() # 确定
driver.close()
