# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:36
# @abstract    :

import pickle
import hashlib
#URL管理器

class UrlManager(object):
	def __init__(self):
		self.undo_urls = self.load_progress('D:/d/spider/20171211/undo_urls.txt')
		self.done_urls = self.load_progress('D:/d/spider/20171211/done_urls.txt')

	def is_or_not_new_url(self): #判断是否有未爬取的url，即爬取是否完毕
		return self.undo_urls_size() !=0

	def get_undo_url(self): #url从undo到done集合转移
		new_url = self.undo_urls.pop()
		m = hashlib.md5()
		m.update(new_url)
		self.done_urls.add(m.hexdigest()[8:-8])
		return new_url

	def add_url_to_undo_urls(self, url): #添加单个的url
		if url is None:
			return
		m = hashlib.md5()
		m.update(url)
		self.done_urls.add(m.hexdigest()[8:-8])
		url_md5 = m.hexdigest()[8:-8]
		if url not in self.undo_urls and url_md5 not in self.done_urls:
			self.undo_urls.add(url)

	def add_urls_to_undo_urls(self, urls): #urls中的每个url，调用add_url_to_undo_urls方法
		if urls is None or len(urls) == 0: # if urls:
			return
		for url  in urls:
			self.add_url_to_undo_urls(url)

	def undo_urls_size(self): #未爬取的url集合大小
		return len(self.undo_urls)

	def done_urls_size(self): #已爬取的url集合大小
		return len(self.done_urls)

	def save_progress(self, path, data):
		with open(path, 'wb') as f:
			pickle.dump(data, f)

	def load_progress(self, path):
		print('[+] 从文件加载进度：%s' %path)
		try:
			with open(path, 'rb') as f:
				tmp = pickle.load(f)
				return tmp
		except:
			print('[!] 无进度文件，创建：%s' %path)
			return set()