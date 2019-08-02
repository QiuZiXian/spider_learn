# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/22  21:18
# @abstract    :

#HTML下载器
import requests

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			return None
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		headers = {"User-Agent":user_agent}
		r = requests.get(url, headers = headers)
		if r.status_code == 200:
			r.encoding = "utf-8" #可引入chardet检测编码进行优化r.encoding = chardet.detect(r.content)["encoding"]
			return r.text
		return None