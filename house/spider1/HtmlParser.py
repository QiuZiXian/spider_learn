# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:37
# @abstract    :

#HTML解析器
import re
from urllib import parse
from bs4 import BeautifulSoup

class HtmlParser(object):

	def parser(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href = re.compile(r'/item/.+'))
		# print("**", links)
		for link in links:
			new_url = link['href']
			new_full_url = parse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		data = {}
		data['url'] = page_url
		title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
		data['title'] = title.get_text()
		summary = soup.find('div', class_='lemma-summary')
		data['summary'] = summary.get_text()
		return data