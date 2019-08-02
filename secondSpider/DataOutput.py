# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:35
# @abstract    :

#数据存储器
import codecs, time, os

class DataOutput(object):

	def __init__(self):
		self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
		self.output_head(self.filepath)
		self.datas = []

	def store_data(self, data):
		if data is None:
			return
		self.datas.append(data)
		if len(self.datas) > 10:
			self.output_html(self.filepath)

	def output_head(self, path):
		fout = codecs.open(path, 'w', encoding="utf-8")
		fout.write("<html>")
		fout.write("<head><meta charset='utf-8'/></head>")
		fout.write("<body>")
		fout.write("<table>")
		fout.close()

	def output_html(self, path):
		pathfile = os.path.join("D:/d/spider/20171211/", path)
		fout = codecs.open(pathfile, 'w', encoding="utf-8")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data["url"])
			fout.write("<td>%s</td>"%data["title"])
			fout.write("<td>%s</td>"%data["summary"])
			fout.write("<tr>")
			self.datas.remove(data)
		fout.close()

	def output_end(self, path):
		fout = codecs.open(path, 'a', encoding="utf-8")
		fout.write("<table>")
		fout.write("</body>")
		fout.write("<html>")
		fout.close()