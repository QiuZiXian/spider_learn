# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/1  18:20
# @abstract    :
import multiprocessing, threading
from zonghengtxt.HtmlDownloader import HtmlDownloader
from zonghengtxt.HtmlParser import HtmlParser
from zonghengtxt.DataOutput import DataOutput

thStart = False
class proMain(object):

	def __init__(self):
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()

	def threadSub(self):
		pass

	def proSub(self, item):
		tomeName = item["tomeName"]
		content = item["content"]
		while content:
			nameAndUrl = content.pop()
			# if not nameAndUrl["vip"]:
			chapter = nameAndUrl["chapterName"]
			url = nameAndUrl["href"]
			html_cont = self.downloader.download(url)
			if html_cont:
				try:
					readtxt = self.parser.getReadText(html_cont)
					self.output.dataToTxt(tomeName, chapter, readtxt)
				except:
					pass

	def proLoadMain(self, allCharpter):
		ps = []
		for item in allCharpter:
			# if not item["all_vip"]:
			p = multiprocessing.Process(target=self.proSub, args=(item,))
			ps.append(p)
		if ps:
			if len(ps) <= 3:
				thStart = True
			for p in ps :
				p.damemon = True
				p.start()
			for p in ps:
				p.join()