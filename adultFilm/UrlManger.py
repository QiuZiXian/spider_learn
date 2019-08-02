# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:36
# @abstract    :

#URL管理器

class UrlManager(object):
	def __init__(self):
		self.undo_urls = {"en":set()}
		self.done_urls = {"en":set()}

	def is_or_not_new_url(self, catagory): #判断是否有未爬取的url，即爬取是否完毕
		return self.undo_urls_size()[catagory] !=0

	def get_undo_url(self, catagory): #url从undo到done集合转移
		new_url = self.undo_urls[catagory].pop()
		self.done_urls[catagory].add(new_url)
		return new_url

	def add_url_to_undo_urls(self, url, catagory): #添加单个的url
		if url is None:
			return
		if url not in self.undo_urls[catagory] and url not in self.done_urls[catagory]:
			self.undo_urls[catagory].add(url)

	def add_urls_to_undo_urls(self, urls, catagory): #urls中的每个url，调用add_url_to_undo_urls方法
		if urls is None or len(urls) == 0: # if urls:
			return
		for url  in urls:
			self.add_url_to_undo_urls(url, catagory)

	def undo_urls_size(self): #未爬取的url集合大小
		undo_size = { catagory: len(links) for catagory, links in self.undo_urls.items()}
		undo_total = sum([undo_size[key] for key in undo_size])
		undo_size["total"] = undo_total
		return undo_size

	def done_urls_size(self): #已爬取的url集合大小
		done_size = { catagory: len(links)for catagory, links in self.done_urls.items()}
		done_total = sum([done_size[key] for key in done_size])
		done_size["total"] = done_total
		return done_size