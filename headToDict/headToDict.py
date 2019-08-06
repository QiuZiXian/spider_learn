# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/22  21:23
# @abstract    :

import re

headers = (
'''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Cookie:_ga=GA1.2.1053266000.1564734163; _gid=GA1.2.979133678.1564734163
Host:fz.maitian.cn
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER
'''
)

def headToDict(headers):
	headers_dict = {}
	headers_list = headers.split("\n")
	for item in headers_list:
		# print(item)
		if item:
			try:
				headers_dict[item.split(':', 1)[0]] = item.split(':', 1)[1]
			except:
				pass
	if headers_dict:
		print('{')
		for item in headers_dict.items():
			print(str(item).lstrip('(').rstrip(')').replace(',', ':'), ',')
		print('}')
	return headers_dict

if __name__ == '__main__':
	print(headToDict(headers))
