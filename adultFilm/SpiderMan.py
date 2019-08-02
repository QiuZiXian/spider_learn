# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:49
# @abstract    :

#爬虫调度器

from adultFilm.DataOutput import DataOutput
from adultFilm.HtmlDownloader import HtmlDownloader
from adultFilm.HtmlParser import HtmlParser
from adultFilm.UrlManger import UrlManager
import time

class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
		self.film_links = {}
		self.crawlDownFilmUrl = {}

	def crawl(self, root_url):
		html_cont = self.downloader.download(root_url)
		catagoryAndpages_dict,titleAndlinks, catagorys = self.parser.parser(root_url, html_cont)
		self.manager.done_urls = {catagory:set() for catagory in catagorys}
		self.film_links = self.parser._getfilmdown_urls(root_url, titleAndlinks["网站首页"])
		self.output.store_data(self.film_links, "网站首页")
		# self.manager.done_urls["网站首页"] = set(root_url)
		# self.output.store_data(titleAndlinks["网站首页"])
		# self.manager.done_urls["网站首页"] = set(root_url)
		self.manager.undo_urls = {catagory:set() for catagory in catagorys}
		for catagory, page_urls in catagoryAndpages_dict.items():
			self.manager.add_urls_to_undo_urls(page_urls, catagory)
		while (self.manager.is_or_not_new_url("total") and self.manager.done_urls_size()["total"] < 1000):#页码
			catagory = catagorys.pop()
			# print(catagorys)
			self.crawlDownFilmUrl[catagory] = 0
			while self.manager.is_or_not_new_url(catagory):
				page_url =  self.manager.get_undo_url(catagory) #某一页链接
				# try:
				new_html = self.downloader.download(page_url)
				titleAndlinks[catagory] = self.parser._getFilm_urls(new_html) # 该页链接的所有film标题和链接
				#根据film链接找到对应的下载链接
				self.film_links = self.parser._getfilmdown_urls(root_url, titleAndlinks[catagory])
				self.output.store_data(self.film_links, catagory)
				self.crawlDownFilmUrl[catagory] += len(self.film_links)
				if self.crawlDownFilmUrl[catagory]%(3 * len(self.film_links)) == 0:
					total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
					print("已爬取%s个链接"%total)
				# except Exception as e:
				# 	print(e)
				# 	print("crawl failed!")
		total = sum([self.crawlDownFilmUrl[key] for key in self.crawlDownFilmUrl])
		print("共爬取%s页,共计%s+%s个链接"%(self.manager.done_urls_size()["total"], total, "0"))


if __name__ == '__main__':
	startt = time.time()
	spider_man = SpiderMan()
	spider_man.crawl("https://www.1551v.com") #/view/10812319.htm;284853
	# spider_man.output.toLoadcsv("load")
	endt = time.time()
	print("本次爬虫共耗时%s,合%s分钟"%((endt - startt), (endt - startt)/60))