# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/8/2  11:25
# @abstract    :

import requests
from bs4 import BeautifulSoup

import time   # 控制爬虫速度
import random # 产生随机数，控制爬虫随机停止时间
from house.spider1.HtmlDownloader import HtmlDownloader # 调 url，get请求
from house.spider1.DataOutput import DataOutput # 调 写函数，存储文件

#实例化
downloader = HtmlDownloader()
output = DataOutput()

url = "http://fz.maitian.cn/zfall" # 麦田网，福州地区租房信息

# r = requests.get(url)
def parser(url):	# 网页解析，这里暂时先不调用已写的包
	r = downloader.download(url)
	# parser

	soup = BeautifulSoup(r, "html.parser") # , from_encoding = "utf-8"

	lis = soup.find_all("li", class_ = "clearfix")
	for li in lis:

		h1 = li.find("div", class_ = "list_title").a.get_text() # 小区名（租房名和房型）
		# 月租，房型，其他，地址
		info = [span.text for span in li.find("div", class_ = "list_title").find_all('span')]
		# print(h1, "".join(info))
		output.store_data("{0} {1}".format(h1, "".join(info)))

# parser(url)
for page in range(0, 10):  # 暂时不单独做spiderman包。循环，爬取所有页面
	try:
		parser("{0}/PG{1}".format(url, page))
		time.sleep(random.randint(5, 10))
	except:
		print(len(output.datas))
		break

output.output_csv(output.write_in_lines(output.datas))
print("ok!")
# page = soup.find("div", class_ = "paging clearfix")
# wei_ye = page.find_all('a')[-1]["href"] # 尾页， /zfall/PG100

'''

                                        香江红海园2期 2室2厅

                                     300089㎡2室2厅1卫2阳居家整租低楼层8层有电梯南北

                                        香江红海园2期金山 金山公园,金桔路, 仓山区金山街道滨州路150号

'''
