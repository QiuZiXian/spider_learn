# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/26  21:43
# @abstract    :

from selenium import webdriver

url = "https://www.1551v.com"

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(url)
div = browser.find_elements_by_class_name("nav_menu")
# print(div)
nav = []
for lu in div:
	lis = lu.find_elements_by_tag_name('li')
	for li in lis:
		try:
			nav.append((li.text, li.find_element_by_tag_name('a').get_attribute('href')))
		except:
			pass
# print(nav)
# nav = [('网站首页', 'https://www.1557v.com/'), ('国产精品', 'https://www.1557v.com/Html/60/'), ('亚洲无码', 'https://www.1557v.com/Html/110/'), ('欧美性爱', 'https://www.1557v.com/Html/62/'), ('VR虚拟现实', 'https://www.1557v.com/Html/86/'), ('成人动漫', 'https://www.1557v.com/Html/101/'), ('自拍图片', 'https://www.1557v.com/Html/63/'), ('情色小说', 'https://www.1557v.com/Html/84/'), ('自拍偷拍', 'https://www.1557v.com/Html/89/'), ('夫妻同房', 'https://www.1557v.com/Html/87/'), ('开放90后', 'https://www.1557v.com/Html/93/'), ('换妻游戏', 'https://www.1557v.com/Html/90/'), ('网红主播', 'https://www.1557v.com/Html/91/'), ('手机小视频', 'https://www.1557v.com/Html/88/'), ('明星艳照门', 'https://www.1557v.com/Html/92/'), ('经典三级', 'https://www.1557v.com/Html/109/'), ('S级女优', 'https://www.1557v.com/Html/100/'), ('波多野结衣', 'https://www.1557v.com/Html/94/'), ('吉泽明步', 'https://www.1557v.com/Html/95/'), ('苍井空', 'https://www.1557v.com/Html/96/'), ('宇都宮紫苑', 'https://www.1557v.com/Html/128/'), ('天海翼', 'https://www.1557v.com/Html/98/'), ('水菜麗', 'https://www.1557v.com/Html/127/'), ('泷泽萝拉', 'https://www.1557v.com/Html/123/'), ('下载区', 'https://www.989bt.com/'), ('无码BT', 'https://www.989bt.com/'), ('有码BT', 'https://www.989bt.com/'), ('皇冠体育', 'https://www.78hgvip.com/main.html'), ('皇冠正网', 'https://www.78hgvip.com/main.html'), ('皇冠赌场', 'https://www.78hgvip.com/main.html'), ('澳门太阳城', 'https://www.11tycvip.com/main.html?m=reg'), ('太阳城赌场', 'https://www.11tycvip.com/main.html?m=reg'), ('无码在线', 'https://www.1557v.com/Html/110/'), ('熟女人妻', 'https://www.1557v.com/Html/111/'), ('美颜巨乳', 'https://www.1557v.com/Html/112/'), ('颜射吃精', 'https://www.1557v.com/Html/113/'), ('丝袜制服', 'https://www.1557v.com/Html/114/'), ('高清无码', 'https://www.1557v.com/Html/130/'), ('中字有码', 'https://www.1557v.com/Html/131/'), ('帮助教程', 'https://www.1557v.com/help.html')]
catagory_urls = [(title, link) for title, link in nav if link[-2].isdigit()]
print(catagory_urls)
browser.close()
