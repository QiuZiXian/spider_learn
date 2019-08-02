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
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		refer = "http://www.bimclub.cn/api/comment.php?mid=15&itemid=1273"
		headers = {"User-Agent":user_agent,
				   "Referer": refer}
		r = requests.get(url, headers = headers)
		if r.status_code == 200:
			r.encoding = "utf-8" #可引入chardet检测编码进行优化r.encoding = chardet.detect(r.content)["encoding"]
			return r.text
		return None

if __name__ == '__main__':
	dowmloader = HtmlDownloader()
	url = "http://www.bimclub.cn/down/down.php?itemid=1273" #http://www.bimclub.cn/down/down.php?itemid=1273
	print(dowmloader.download(url))
