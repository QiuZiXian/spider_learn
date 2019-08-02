# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/13  20:53
# @abstract    :

import csv, os,json

class DataOutput_2(object):

	def __init__(self):
		self.errors = [{"_parser_release":[]}, {"_parser_no_release":[]}]
		self.datas = []
		self.csv_header = ("电影id", "电影名称", "综合评分", "音乐评分", "画面评分", "导演评分", "故事评分","参与评分人数", "想看的人数", "总票房", "今日票房", "排名","上映时间", "isrelease")


	def store_data(self,data):
		if data is None:
			return
		if len(data) <=4: # (isRelease, e, page_url, value)
			self.errors[0]["_parser_release"].append({"isRelease":data[0], "Exception":"{}".format(data[1]), "page_url":data[2], "value":data[3]})
		else:
			self.datas.append(data)
		if len(self.datas) > 10:
			self.output_csv('MTime')

	def output_csv(self, csv_name):
		# pathfile = os.path.join("D:/d/spider/20171211/mtime", "{0}.csv".format(csv_name))
		if not os.path.exists("D:/d/spider/20171211/mtime/20171214.csv"):
			f = open("D:/d/spider/20171211/mtime/20171214.csv", "w")
			writer = csv.writer(f)
			writer.writerow(self.csv_header)
			f.close()
		else:
			with open("D:/d/spider/20171211/mtime/20171214.csv", 'a+') as f:
				writer = csv.writer(f)
				writer.writerows(self.datas)
				self.datas = []

	def save_errors(self):
		print(self.errors)
		with open("D:/d/spider/20171211/mtime/20171214.json", "w") as fp:
			json.dump(self.errors, fp = fp, indent= 4, ensure_ascii=False)


