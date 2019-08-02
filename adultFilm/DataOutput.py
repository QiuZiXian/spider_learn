# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:35
# @abstract    :

#数据存储器
import codecs, time, os, csv
import urllib

class DataOutput(object):

	def __init__(self):
		self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
		self.datas = []

	def store_data(self, data, catagory):
		if not data and len(data)>3 :
			return
		self.dataTocsv(data, catagory)

	def dataTocsv(self, data, catagory):
		with open("D:/d/spider/adult-movies/data/{0}.csv".format(catagory), "a") as fcsv:
			csvwriter = csv.writer(fcsv)
			csvwriter.writerows(data)
			# for title, titleAndlink in data.items():
			# 	csvwriter.writerow([title])
			# 	csvwriter.writerows(titleAndlink)

	def toLoadcsv(self, filename):
		with open("D:/d/spider/adult-movies/data/seed-2.csv", "r") as fcsv:
			csvreader = csv.reader(fcsv)
			rows = [ row for row in csvreader if row]
			print(rows)

	def dowloadFilms(self, title, filmDownUrl):
		def Schedule( a,b,c):
			'''''
			a:已经下载的数据块
			b:数据块的大小
			c:远程文件的大小
		   '''
			per = 100.0 * a * b / c
			if per > 100 :
				per = 100
			# if per/10
			print ('%.2f%%' % per)
		filename = os.path.join("D:/d/spider/adult-movies", "{0}.mp4".format(title))
		urllib.request.urlretrieve(filmDownUrl, filename, Schedule)

	def dowloadFic(self, title, cont):
		with open("D:/d/spider/adult-movies/download/情色小说/{}.txt".format(title), "w", encoding="utf-8") as f:
			f.write(cont)
