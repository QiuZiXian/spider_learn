# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:35
# @abstract    :

#数据存储器
import codecs

class DataOutput(object):

	def __init__(self):
		self.datas = []

	def store_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = codecs.open("D:/d/spider/20171208/baike/baike.html", 'w', encoding="utf-8")
		fout.write("<html>")
		fout.write("<head><meta charset='utf-8'/></head>")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data["url"])
			fout.write("<td>%s</td>"%data["title"])
			fout.write("<td>%s</td>"%data["summary"])
			fout.write("<tr>")
			self.datas.remove(data)
		fout.write("<table>")
		fout.write("<body>")
		fout.write("<html>")
		fout.close()