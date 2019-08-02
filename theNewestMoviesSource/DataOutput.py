# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/3/5  19:30
# @abstract    :

import csv, chardet, os
path = "D:/d/spider/movieSource/"

class DataOutput(object):

	def dataTocsv(self, data):
		if data:
			try:
				with open("D:/d/spider/movieSource/test.csv", "a", encoding="utf-8") as fcsv:
					csvwriter = csv.writer(fcsv)
					csvwriter.writerows(data)
			except:
				print(data)

	def toLoadcsv(self):
		with open("D:/d/spider/movieSource/test.csv", "r", encoding="utf-8") as fcsv:
			csvreader = csv.reader(fcsv)
			rows = [row for row in csvreader if row]
		return rows