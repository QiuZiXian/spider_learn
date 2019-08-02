# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/2  14:27
# @abstract    :

from selenium import webdriver
from zonghengtxt.DataOutput import DataOutput
# driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
output = DataOutput()
url = "http://www.zongheng.com/mianfei/"
# print(html_cont)
driver.get(url)
driver.implicitly_wait(5)
tab_cont5 = driver.find_element_by_xpath(".//*[@id='clk_rco_xinshu']") # 免费小说新书版
tab_cont2 = driver.find_element_by_xpath("html/body/div[6]/div[2]/div[2]/div[3]") # 免费小说强推版 ,！！两个a

tab_cont = driver.find_element_by_xpath("html/body/div[6]/div[2]/div[2]/div[1]") # 免费小说点击版日
tab_cont3 = driver.find_element_by_xpath("html/body/div[6]/div[2]/div[2]/div[5]") # 免费小说收藏版
tab_cont4 = driver.find_element_by_xpath("html/body/div[10]/div[2]/div[1]") # 免费小说红票版
tab_cont7 = driver.find_element_by_xpath("html/body/div[6]/div[1]/div[5]") # 免费小说txt下载榜

tab_cont6 = driver.find_element_by_xpath("html/body/div[6]/div[1]/div[3]") # 百万字免费小说 ！！无top
tabsXpath = [tab_cont, tab_cont3, tab_cont4,tab_cont6, tab_cont7]
tabsXpath2 = [tab_cont2, tab_cont5]
timeToFree = driver.find_element_by_xpath("html/body/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/h3")

def parser(tab_cont):
	title_cont = tab_cont.find_elements_by_css_selector("span")
	cont = set()
	for item in title_cont:
		try:
			if item.text.isdigit():
				continue
			tabtitle = item.text
		except:
			tabtitle = "分类标题丢失"
			continue
	results = tab_cont.find_elements_by_css_selector("li")
	for result in results:
		try:
			top = result.find_element_by_tag_name("em").text
		except:
			top = False
		url = result.find_element_by_tag_name('a').get_attribute("href")
		ficName = result.find_element_by_tag_name('a').get_attribute("title")
		cont.add((url, top, ficName))
	tablists = [{"href": url, "top": top, "ficName":ficName} for url, top, ficName in cont]
	# print(cont)
	return tabtitle, tablists
# print(timeToFree.find_element_by_tag_name('a').get_attribute("title"), timeToFree.find_element_by_tag_name('a').get_attribute("href"))
def parser2(tab_cont):
	title_cont = tab_cont.find_elements_by_css_selector("span")
	cont = set()
	for item in title_cont:
		try:
			if item.text.isdigit():
				continue
			tabtitle = item.text
			break
		except:
			tabtitle = "分类标题丢失"
			continue
	results = tab_cont.find_elements_by_css_selector("li")
	for result in results:
		try:
			top = result.find_element_by_tag_name("em").get_attritute("order")
			ficName = result.find_elements_by_css_selector('a')[1].get_attribute("title")
		except:
			top = result.find_elements_by_css_selector('a')[0].text
			ficName = result.find_elements_by_css_selector('a')[1].text
		url = result.find_elements_by_css_selector('a')[1].get_attribute("href")
		cont.add((url, top, ficName))
	tablists = [{"href": url, "top": top, "ficName":ficName} for url, top, ficName in cont]
	return tabtitle, tablists

def parserMain(tabsXpath, tabsXpath2, timeToFree):
	freeCont = []
	for tab_cont in tabsXpath:
		tabTitle, tabLists =  parser(tab_cont)
		freeCont.append({"tabtitle":tabTitle, "tablists":tabLists})

	for tab_cont in tabsXpath2:
		tabTitle, tabLists = parser2(tab_cont2)
		freeCont.append({"tabtitle":tabTitle, "tablists":tabLists})

	tabLists = [{"ficName": timeToFree.find_element_by_tag_name('a').get_attribute("title"),"href": timeToFree.find_element_by_tag_name('a').get_attribute("href"), "top": False}]
	freeCont.append({"tabtitle":"限时免费", "tablists":tabLists})
	return freeCont

freeCont = parserMain(tabsXpath, tabsXpath2, timeToFree)
driver.close()

output.freeContToJson("免费小说首页", freeCont)
print("end!")