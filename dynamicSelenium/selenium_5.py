# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/15  20:08
# @abstract    : 226显示等待

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
url = "https://www.baidu.com" # http://somedomain/url_that_delays_loading错误
driver.get(url)
try:
	elen = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	driver.quit()