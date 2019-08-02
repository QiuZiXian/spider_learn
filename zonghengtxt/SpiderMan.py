# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:49
# @abstract    :

#爬虫调度器

from zonghengtxt.DataOutput import DataOutput
from zonghengtxt.HtmlDownloader import HtmlDownloader
from zonghengtxt.HtmlParser import HtmlParser
from zonghengtxt.proMain import proMain
from zonghengtxt.UrlManger import UrlManager
import time

class SpiderMan(object):
	def __init__(self):
		self.pro = proMain()
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
		self.film_links = {}
		self.crawlDownFilmUrl = {}

	# def crawl(self, root_url, ficName):
	# 	html_cont = self.downloader.download(root_url) # 目录页
	# 	allCharpter = self.parser.getAllCharpter(html_cont)
	# 	self.output.dataToJson(ficName, allCharpter)
	# 	# allCharpter = self.output.loadJson(ficName)
	# 	self.pro.proLoadMain(allCharpter)

	def crawl(self):
		freeCont = self.output.loadJson("免费小说首页")
		hasDoneDict, hasDoneList = self.output.getLocalDoneFic()
		# print(freeCont)
		self.manager.undo_urls = {tabTitleAndLists["tabtitle"]:tabTitleAndLists["tablists"] for tabTitleAndLists in freeCont }
		for key, values in self.manager.undo_urls.items(): # 根据本地数据进行更新
			for item in values:
				if item["ficName"] in hasDoneList:
					values.pop(values.index(item))
		# print(self.manager.undo_urls)
		self.manager.done_urls = set()
		while (self.manager.is_or_not_new_url("total") and self.manager.done_urls_size() < 100):
			for key in self.manager.undo_urls.keys(): # key的值为tabtitle
				# print(key)
				try:
					tablist = self.manager.get_undo_url(key)
					# TODO 查重有问题，待考虑
					# if (tablist["href"], tablist["ficName"]) in self.manager.done_urls:
					# 	continue
					root_url = tablist["href"].replace("/book/", "/showchapter/")
					html_cont = self.downloader.download(root_url) # 目录页
					allCharpter = self.parser.getAllCharpter(html_cont)
					if tablist["top"]:
						tablist["ficName"] = tablist["top"] + tablist["ficName"]
					self.output.charpterToJson(key ,tablist["ficName"], allCharpter)
				# allCharpter = self.output.loadJson(ficName)
					self.pro.proLoadMain(allCharpter)
					self.manager.doneOrFalse(key, True)
				except:
					self.manager.doneOrFalse(key, False)
					print("crawl failed")
		print("共爬取{0}部小说如下{1}".format(self.manager.done_urls_size(), "-".join([item[1] for item in self.manager.done_urls])))
		try:
			self.output.freeContToJson("errors", [self.manager.errors])
		except:
			pass

if __name__ == '__main__':
	startt = time.time()
	spider_man = SpiderMan()
	# root_url = "http://book.zongheng.com/showchapter/189169.html"
	# ficName = "雪中悍刀行"
	# root_url = "http://book.zongheng.com/showchapter/385404.html"
	# ficName = "都市最强修真"
	# spider_man.crawl(root_url, ficName) #/view/10812319.htm;284853
	# spider_man.output.toLoadcsv("load")
	spider_man.crawl()
	endt = time.time()
	print("本次爬虫共耗时%s,合%s分钟"%((endt - startt), (endt - startt)/60))