# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/3/5  18:36
# @abstract    :

from theNewestMoviesSource.HtmlDownloader import HtmlDownloader
from theNewestMoviesSource.HtmlParser import HtmlParser
from theNewestMoviesSource.DataOutput import DataOutput
from urllib import parse
import time

class SpiderMan(object):

	def __init__(self):
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
		self.total = 0

	def mainCrawl(self, root_url, stop = False):
		page = 1
		while not stop and page <=10:
			reqt = self.downloader.download(root_url)
			new_urls, uploadTimes = self.parser.parserPage(reqt)
			# print(new_urls, len(new_urls))
			if new_urls: # 单页的所有rows信息有提取到
				data = []
				for url in set(new_urls):
					newUrl = parse.urljoin("http://r2.1024cls.pw/pw/", url)
					reqt = self.downloader.download(newUrl)
					movieTitle, movieUrl, movieMessage = self.parser.parser(reqt)
					time.sleep(0.02)
					if movieUrl:
						data.append([movieTitle, movieUrl])
				# print(data, len(data))
				self.total += len(data)
				self.output.dataTocsv(data)
			if not stop:
				page += 1
				root_url =  "{0}&page={1}".format(root_url, page)
		print("end!")

if __name__ == '__main__':
	startt = time.time()
	root_url = "http://r2.1024cls.pw/pw/thread.php?fid=83"
	spider_man = SpiderMan()
	spider_man.mainCrawl(root_url)
	endt = time.time()
	print("the crawl get %s pieces moviesData"%spider_man.total)
	print("the crawl cost %s secends time"%(endt - startt))