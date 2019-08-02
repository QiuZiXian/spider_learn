# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/28  11:49
# @abstract    :

#爬虫调度器

from adultFilm.DataOutput import DataOutput
from adultFilm.HtmlDownloader import HtmlDownloader
from adultFilm.HtmlParser import HtmlParser
from adultFilm.UrlManger import UrlManager
import time, threading

L_filmUrl = threading.Lock()
L_catagory = threading.Lock()
L_th = threading.Lock()

class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
		self.film_links = ["test"]
		self.crawlDownFilmUrl = {}

	def producerth(self, root_url, page_url):
		# print(self.film_links)
		new_html = self.downloader.download(page_url)
		titleAndlinks = self.parser._getFilm_urls(new_html) # 该页链接的所有film标题和链接
		#根据film链接找到对应的下载链接
		self.film_links = self.parser._getfilmdown_urls(root_url, titleAndlinks)
	# print(threading.current_thread().name, len(self.film_links))

	def consumerth(self, catagory):
		self.output.store_data(self.film_links, catagory)
		self.crawlDownFilmUrl[catagory] += len(self.film_links)
		if self.crawlDownFilmUrl[catagory]%(3 * 12) == 0:
			total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
			print("已爬取%s个链接"%total)
		# print(threading.current_thread().name, catagory)

	def crawl(self, root_url):
		html_cont = self.downloader.download(root_url)
		catagoryAndpages_dict,titleAndlinks, catagorys = self.parser.parser(root_url, html_cont)
		self.manager.done_urls = {catagory:set() for catagory in catagorys}
		# self.film_links = self.parser._getfilmdowm_urls(root_url, titleAndlinks["网站首页"])
		# self.output.store_data(self.film_links, "网站首页")
		self.manager.undo_urls = {catagory:set() for catagory in catagorys}
		for catagory, page_urls in catagoryAndpages_dict.items():
			self.manager.add_urls_to_undo_urls(page_urls, catagory)
		while (self.manager.is_or_not_new_url("total") and self.manager.done_urls_size()["total"] < 1000):#页码
			# print(catagorys)
			while self.manager.is_or_not_new_url("total"):
				L_catagory.acquire()
				catagory = catagorys.pop()
				self.crawlDownFilmUrl[catagory] = 0
				L_catagory.release()
				threads = []
				L_th.acquire()
				for i in range(5):
					# print(self.manager.undo_urls)
					if self.manager.undo_urls_size()[catagory]:
						page_url =  self.manager.get_undo_url(catagory) #某一页链接
						th = threading.Thread(target=self.threadmain, name="{}".format(i), args=(root_url, page_url, catagory))
						threads.append(th)
					else:
						break
				L_th.release()
				if threads:
					for th in threads:
						th.start()
					for th in threads:
						th.join()
					# print(e)
		total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
		print("共爬取%s页,共计%s+%s个链接"%(self.manager.done_urls_size()["total"], total, "0"))

	def threadmain(self, root_url, page_url, catagory):
		try:
			L_filmUrl.acquire()
			t = threading.Thread(target=self.producerth, name="pro", args=(root_url, page_url))
			L_filmUrl.release()
			L_filmUrl.acquire()
			t2 = threading.Thread(target=self.consumerth,name="con", args=(catagory,))
			L_filmUrl.release()
			t.start()
			t.join()
			t2.start()
			t2.join()
		except Exception as e:
			# print("crawl failed!")
			pass
		print(threading.current_thread().name, len(self.film_links), "main")

if __name__ == '__main__':
	startt = time.time()
	spider_man = SpiderMan()
	spider_man.crawl("https://www.1551v.com") #/view/10812319.htm;284853
	# spider_man.output.toLoadcsv("load")
	endt = time.time()
	print("本次爬虫共耗时%s,合%s分钟"%((endt - startt), (endt - startt)/60))