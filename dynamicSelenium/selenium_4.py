# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/15  18:54
# @abstract    : P222，页面操作

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
url = "https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F%3Fex_track%3Dauto_4ef180cc"
driver.get(url)
driver.implicitly_wait(5)
print(driver.title)
username = driver.find_element_by_name("username")
passward = driver.find_element_by_name("password")
vcode = driver.find_element_by_name("vcode")
username.clear()
username.send_keys("123")
passward.clear()
passward.send_keys("123")
vcode.clear()
vcode.send_keys("123")
time.sleep(5)
try:
	btn = driver.find_element_by_class_name("new-login-btn")
	# btn.send_keys(Keys.RETURN) # 这里btn用鼠标点击而不能submit，文本框输入后才能submit
	btn.click()
	print("*")
except:
	try:
		btn = driver.find_element_by_xpath("//input[@type='submit']")
		print("**")
		btn.send_keys(Keys.RETURN)
	except:
		print("***")



time.sleep(20)
driver.close()


