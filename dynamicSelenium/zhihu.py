# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/16  16:41
# @abstract    : 网页登陆(知乎)

import re
import requests

def get_xsrf(session):
	index_url = "http://www.zhihu.com"
	index_page = session.get(index_url, headers = headers)
	html = index_page.text
	pattern = r'name="_xsrf" value="(.*?)"' # type="hidden" value="(.*?)"
	_xsrf = re.findall(pattern, html)
	return _xsrf[0]

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
headers = {'User-Agent':agent}
session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'https://www.zhihu.com/login/phone_num'
postdata = {
	'_xsrf':_xsrf,
	'password': 'hai!SHUI249114',
	'remember_me':'true',
	'phone_num':'13055415855'
}
login_page = session.post(post_url, data=postdata, headers= headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)



