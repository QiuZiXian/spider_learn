# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/3/5  15:43
# @abstract    :

import requests

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			return None
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		headers = {"User-Agent":user_agent}
		req = requests.get(url, headers=headers)
		if req.status_code == 200:
			req.encoding = "utf-8"
			return req.text
		return None