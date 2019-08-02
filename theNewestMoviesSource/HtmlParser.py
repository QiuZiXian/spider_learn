# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/3/5  15:47
# @abstract    :

from theNewestMoviesSource.HtmlDownloader import HtmlDownloader

import re

class HtmlParser(object):

	def parserPage(self, reqt): # 翻页及页面信息提取
		try:
			pageUrls = re.findall(r'href="(htm_data/83/.*?\.html)"', reqt)
			uploadtTime = re.findall(r'<a href="read\.php\?tid=\d*?\&page=e\&fpage=\d*?\#a" class="f10"> (.*?) </a>', reqt)
		except:
			pageUrls, uploadtTime = None, None
		# print(len(pageUrls), pageUrls)
		# print(len(uploadtTime), uploadtTime)
		return pageUrls, uploadtTime

	def parser(self, reqt): # 电影链接及相关信息提取
		# moviesUrl = re.search(r'href="http://www3\.uptorrentfilespacedownhostabc\.biz/updowm/file\.php/P50DHBl\.html"', reqt).group(0)
		# print(reqt)
		# return
		try:
			moviesUrl = re.search(r'href="(http://www3\..*?\.html)"', reqt).group(1)
			moviesTitle = re.search(r'<h1 id="subject_tpc" class="fl">&nbsp;(.*?)</h1>', reqt).group(1)
		except:
			moviesUrl, moviesTitle = None, None
		try:
			moviesMessage = re.search(r'◎译　　名　(.*?)<br>◎片　　名　(.*?)<br>◎年　　代　(.*?)<br>◎产　　地　(.*?)<br>◎类　　别　(.*?)<br>◎语　　言　(.*?)<br>◎上映日期　(.*?)<br>◎IMDb评分&nbsp;&nbsp;(.*?)<br>◎IMDb链接&nbsp;&nbsp;<a href="(.*?)" target="_blank">http://www.imdb.com/title/tt5846644/</a><br>◎豆瓣评分　(.*?)<br>◎豆瓣链接　<a href="(.*?)" target="_blank">https://movie.douban.com/subject/26827040/</a><br>◎片　　长　(.*?)<br>◎导　　演　(.*?)<br>◎主　　演　(.*?)<br><br>◎简　　介<br><br>(.*?)<br><br><br><img', reqt, re.S).groups()
		# 译名；片名；年代；产地；类别；语言；上映日期；IMDb评分；IMDb链接；豆瓣评分；豆瓣链接；片长；导演；主演；简介
		except:
			moviesMessage = "default"
		# print(moviesUrl, moviesTitle, moviesMessage)
		return moviesUrl, moviesTitle, moviesMessage

if __name__ == '__main__':
	url = "http://r2.1024cls.pw/pw/htm_data/83/1803/1036369.html"
	pageUrl = "http://r2.1024cls.pw/pw/thread.php?fid=83&page=5"
	# reqt = downloader.download(url)
	downloader = HtmlDownloader()

	reqt = downloader.download(pageUrl)
	example = HtmlParser()
	OnePageAllMovieUrls = example.parserPage(reqt)
	# moviesUrl = example.parser(reqt)