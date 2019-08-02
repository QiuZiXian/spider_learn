# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/1  14:17
# @abstract    :

from zonghengtxt.HtmlDownloader import HtmlDownloader
from bs4 import BeautifulSoup
import re
import json

downloader = HtmlDownloader()

url = "http://book.zongheng.com/chapter/385539/6610244.html"
# html_cont = downloader.download(url)
# print(html_cont)
# title_cont = re.search(r'<h1>(.+?)</h1>', html_cont).group(1)
# print(title_cont)
# title = re.search(r'<em itemprop="headline">(.+?)</em>', title_cont).group(1)
# # print(title)
# readtxt_cont = re.search(r'<div id="readerFs" class="">(.+?)<!-- 底部文字链推广位 -->', html_cont, re.S).group(1)
# readtxt = re.findall(r'<p>(.+?)</p>', readtxt_cont)
# print(readtxt, len(readtxt))
# # title = "test"
# with open("D:/d/spider/zonghengtxt/{}.txt".format(title), "w", encoding="utf-8") as f:
# 	for line in readtxt:
# 		f.writelines("  {}".format(line))
# 		f.writelines("\n")
# print("end!")


url = "http://book.zongheng.com/showchapter/278467.html"
html_cont = downloader.download(url)
# print(html_cont)
# html_path = etree.HTML(html_cont)
# catagorys = html_path.xpath(".//*[@id='chapterListPanel']/h5[2]")
catagorys = re.findall(r'<h5 class="chap_li">(.+?)<div class="shade_one">', html_cont, re.S)
# print(catagorys, len(catagorys))
mu_cont = re.findall(r'<div class="cl20">(.+?)</table>', html_cont, re.S)
# print(mu_cont, len(mu_cont))
readtxt = []
for mus in mu_cont:
	# print(mus)
	catagory = re.search(r'tomeName="(.+?)"', mus).group(1)
	print(catagory)
	tds = re.findall(r'<td(.+?)</td>', mus, re.S) # 非vip章节不需要re.S
	# nameAndUrls = [{"vip": (re.search(r'<em class="vip"></em>', td) is not None), "chapterName":re.search(r'chapterName="(.+?)"', td).group(1), "href":re.search(r'href="(.+?)\.html"', td).group(0)} for td in tds]
	# all_vip = True
	# for nameAndUrl in nameAndUrls:
	# 	if not nameAndUrl["vip"]:
	# 		all_vip = False
	# 		break
	# readtxt.append({"all_vip": all_vip, "tomeName": catagory, "content": nameAndUrls})
	for td in tds:
		chapterName = re.search(r'chapterName="(.+?)"', td).group(1)
		url = re.search(r'href="(.+?\.html)"', td).group(1)
		vip = re.search(r'<em class="vip"></em>', tds[-1])
		print(chapterName, url, (vip is None))
	# 	break
	# break
#
# def save_to_json(content):
# 	with open("D:/d/spider/zonghengtxt/雪中悍刀行.json", "w") as fp:
# 		json.dump(content, fp = fp, indent= 4, ensure_ascii=False)
# 	with open("D:/d/spider/zonghengtxt/雪中悍刀行.json", "r") as fp:
# 		print(json.load(fp))
# # save_to_json(readtxt)
