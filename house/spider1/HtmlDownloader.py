# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:38
# @abstract    :

#HTML下载器
import requests

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			return None
		# user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		# headers = {"User-Agent":user_agent}
		headers = {
		'Accept-Language': 'zh-CN:zh;q=0.8' ,
		'Accept-Encoding': 'gzip: deflate: sdch' ,
		'Connection': 'keep-alive' ,
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER' ,
		'Host': 'fz.maitian.cn' ,
		'Accept': 'text/html:application/xhtml+xml:application/xml;q=0.9:image/webp:*/*;q=0.8' ,
		'Cookie': '_ga=GA1.2.1053266000.1564734163; _gid=GA1.2.979133678.1564734163' ,
		'Upgrade-Insecure-Requests': '1' ,
		}
		r = requests.get(url, headers = headers)
		if r.status_code == 200:
			r.encoding = "utf-8" #可引入chardet检测编码进行优化r.encoding = chardet.detect(r.content)["encoding"]
			return r.text
		return None