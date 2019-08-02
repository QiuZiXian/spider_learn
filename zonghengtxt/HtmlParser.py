# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:37
# @abstract    :

#HTML解析器
import re
from urllib import parse
import threading

# film_links = [] # 不会用？？？
L = threading.Lock()

class HtmlParser(object):

	def __init__(self):
		pass
	def parser(self, root_url, html_cont):
		if root_url is None or html_cont is None:
			return

	def getAllCharpter(self, html_cont): # 获取小说的所有章节目录
		mu_cont = re.findall(r'<div class="cl20">(.+?)</table>', html_cont, re.S)
		allCharpter = []
		for mus in mu_cont:
			catagory = re.search(r'tomeName="(.+?)"', mus).group(1)
			# print(catagory)
			tds = re.findall(r'<td(.+?)</td>', mus, re.S) # 非vip章节不需要re.S
			nameAndUrls = [{"vip": (re.search(r'<em class="vip"></em>', td) is not None), "chapterName":re.search(r'chapterName="(.+?)"', td).group(1), "href":re.search(r'href="(.+?\.html)"', td).group(1)} for td in tds]
			all_vip = True
			for nameAndUrl in nameAndUrls:
				if not nameAndUrl["vip"]:
					all_vip = False
					break
			allCharpter.append({"all_vip": all_vip, "tomeName": catagory, "content": nameAndUrls})
		return allCharpter

	def getReadText(self, html_cont):
		# title_cont = re.search(r'<h1>(.+?)</h1>', html_cont).group(1)
		# title = re.search(r'<em itemprop="headline">(.+?)</em>', title_cont).group(1)
		readtxt_cont = re.search(r'<div id="readerFs" class="">(.+?)<!-- 底部文字链推广位 -->', html_cont, re.S).group(1) # 这个还有点小问题
		readtxt = re.findall(r'<p>(.+?)</p>', readtxt_cont)
		# print(readtxt, len(readtxt))
		return readtxt


if __name__ == '__main__':
	pass