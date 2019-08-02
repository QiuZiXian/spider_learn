# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/13  20:16
# @abstract    :

from dynamicSpider.DataOutput_2 import DataOutput_2
from dynamicSpider.HtmlDownloader import HtmlDownloader
from dynamicSpider.HtmlParser import HtmlParser
import time

class SpiderMan(object):

	def __init__(self):
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput_2()
		self.errors = [{"_parser_release":[]}, {"_parser_no_release":[]}]

	def crawl(self, root_url):
		content = self.downloader.download(root_url)
		urls = self.parser.parser_url(root_url, content)
		for url in urls:
			try:
				t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
				rank_url = 'http://service.library.mtime.com/Movie.api' \
						   '?Ajax_CallBack=true' \
						   '&Ajax_CallBackType=Mtime.Library.Services' \
						   '&Ajax_CallBackMethod=GetMovieOverviewRating' \
						   '&Ajax_CrossDomain=1' \
						   '&Ajax_RequestUrl={0}' \
						   '&t={1}' \
						   '&Ajax_CallBackArgument0={2}'.format(url[0], t, url[1])
				# print(rank_url)
				rank_content = self.downloader.download(rank_url)
				# print(rank_content)
				data = self.parser.parser_json(rank_url, rank_content)
				self.output.store_data(data)
			except Exception as e:
				print("Craw failed")
				# print(urls, rank_url)
		try:
			self.output.save_errors()
		except:
			pass
		print("Craw finished")

if __name__ == '__main__':
	spider = SpiderMan()
	spider.crawl('http://theater.mtime.com/China_Beijing/')