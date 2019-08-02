# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:49
# @abstract    :

#爬虫调度器

from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.HtmlParser import HtmlParser
from firstSpider.UrlManger import UrlManager

class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()

	def crawl(self, root_url):
		self.manager.add_url_to_undo_urls(root_url)
		while (self.manager.is_or_not_new_url() and self.manager.done_urls_size() <100):
			try:
				new_url = self.manager.get_undo_url()
				html = self.downloader.download(new_url)
				new_urls, data = self.parser.parser(new_url, html)
				# print(new_urls)
				self.manager.add_urls_to_undo_urls(new_urls)
				self.output.store_data(data)
				print("已抓取%s个链接"%self.manager.done_urls_size())
			except Exception as e:
				print("crawl failed!")
		self.output.output_html()

if __name__ == '__main__':
	spider_man = SpiderMan()
	spider_man.crawl("https://baike.baidu.com/view/284853.htm") #/view/10812319.htm;284853