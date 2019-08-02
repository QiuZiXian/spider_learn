# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:36
# @abstract    :

#URL管理器

class UrlManager(object):
	def __init__(self):
		self.undo_urls = {"en":set()}
		self.done_urls = set()
		self.errors = {}

	def is_or_not_new_url(self, catagory): #判断是否有未爬取的url，即爬取是否完毕
		return self.undo_urls_size()[catagory] !=0

	def get_undo_url(self, catagory): #url从undo到done集合转移
		new_url = self.undo_urls[catagory].pop()
		self.temp = new_url
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
		return len(self.done_urls)

	def doneOrFalse(self, key, boolValue):
		if boolValue:
			self.done_urls.add((self.temp["href"], self.temp["ficName"]))
		else:
			if key in self.errors:
				self.errors[key].append(self.temp)
			else:
				self.errors[key] = [self.temp]

	def errorsHand(self):
		seconFreeCont = []
		for key, values in self.errors.items():
			for item in values:
				seconFreeCont.append(item)
		return [{"tabtitle": "之前错误重试", "tablists": seconFreeCont}]

