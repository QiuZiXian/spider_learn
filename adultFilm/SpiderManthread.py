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
import time, threading, multiprocessing

L = threading.Lock()

class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
		self.film_links = []
		self.crawlDownFilmUrl = {}

	def producerth(self, root_url, filmsUrls):
		# print(self.film_links)
		self.film_links = self.parser._getfilmdown_urls(root_url, filmsUrls)
		# print(threading.current_thread().name, len(self.film_links))

	def consumerth(self, catagory):
		self.output.store_data(self.film_links, catagory)
		self.crawlDownFilmUrl[catagory] += len(self.film_links)
		if self.crawlDownFilmUrl[catagory]%(3 * 12) == 0:
			total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
			print("已爬取%s个链接"%total)
		# print(threading.current_thread().name, catagory)

	def threadFic(self,ficUrls):
		new_html = self.downloader.download(ficUrls[1])
		if new_html:
			cont = self.parser.getFic(new_html)
			self.output.dowloadFic(ficUrls[0], cont)

	def thFicAndPicMain(self, catagory):
		if catagory == "情色小说":
			while self.film_links:
				ps = []
				for i in range(10): # 10个进程
					if self.film_links:
						ficUrls = self.film_links.pop()
						pr = multiprocessing.Process(target=self.threadFic, args=(ficUrls,))
						ps.append(pr)
					else:
						break
				if ps:
					for p in ps:
						p.daemon = True
						p.start()
					for p in ps:
						p.join()
		else: # 图片
			pass

	def crawl(self, root_url):
		html_cont = self.downloader.download(root_url)
		catagoryAndpages_dict,titleAndlinks, catagorys = self.parser.parser(root_url, html_cont)
		self.manager.done_urls = {catagory:set() for catagory in catagorys}
		# self.film_links = self.parser._getfilmdowm_urls(root_url, titleAndlinks["网站首页"])
		# self.output.store_data(self.film_links, "网站首页")
		self.manager.undo_urls = {catagory:set() for catagory in catagorys}
		for catagory, page_urls in catagoryAndpages_dict.items():
			try:
				self.manager.add_urls_to_undo_urls(page_urls, catagory)
			except:
				continue
		while (self.manager.is_or_not_new_url("total") and self.manager.done_urls_size()["total"] < 1000):#页码
			L.acquire()
			catagory = catagorys.pop()
			L.release()
			# print(catagory)
			self.crawlDownFilmUrl[catagory] = 0
			while self.manager.is_or_not_new_url(catagory):
				page_url =  self.manager.get_undo_url(catagory) #某一页链接
				try:
					new_html = self.downloader.download(page_url)
					titleAndlinks[catagory] = self.parser._getFilm_urls(new_html) # 该页链接的所有film标题和链接
					# print(catagory)
					if catagory in ['情色小说', "自拍图片"]:
						self.film_links = self.parser._getPictureOrFiction(root_url, titleAndlinks[catagory])
						self.consumerth(catagory)
						self.thFicAndPicMain(catagory)

						# print(titleAndlinks)
					else:
						#根据film链接找到对应的下载链接
						L.acquire()
						t = threading.Thread(target=self.producerth, name="pro", args=(root_url, titleAndlinks[catagory]))
						L.release()
						L.acquire()
						t2 = threading.Thread(target=self.consumerth,name="con", args=(catagory,))
						L.release()
						t.start()
						t.join()
						t2.start()
						t2.join()
				except Exception as e:
					print(e)
					print("crawl failed!")
		total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
		print("共爬取%s页,共计%s+%s个链接"%(self.manager.done_urls_size()["total"], total, "0"))


if __name__ == '__main__':
	startt = time.time()
	spider_man = SpiderMan()
	spider_man.crawl("https://www.1551v.com") #/view/10812319.htm;284853
	# spider_man.output.toLoadcsv("load")
	endt = time.time()
	print("本次爬虫共耗时%s,合%s分钟"%((endt - startt), (endt - startt)/60))