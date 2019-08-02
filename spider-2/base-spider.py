# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  9:56
# @abstract    :

#URL管理器

class UrlManager(object):
	def __init__(self):
		self.undo_urls = set()
		self.done_urls = set()

	def is_or_not_new_url(self): #判断是否有未爬取的url，即爬取是否完毕
		return self.undo_urls_size() !=0

	def get_undo_url(self): #url从undo到done集合转移
		new_url = self.undo_urls.pop()
		self.done_urls.add(new_url)
		return new_url

	def add_url_to_undo_urls(self, url): #添加单个的url
		if url is None:
			return
		if url not in self.undo_urls and url not in self.done_urls:
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
		return new_data, new_data

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href = re.compile(r'/view/\d+\.htm'))
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

#数据存储器
import codecs

class DataOutput(object):

	def __init__(self):
		self.datas = []

	def store_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = codecs.open("D:/d/spider/20171208/baike/baike.html", 'w', encoding="utf-8")
		fout.write("<html>")
		fout.write("<head><meta charset='utf-8'/></head>")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data["url"])
			fout.write("<td>%s</td>"%data["title"])
			fout.write("<td>%s</td>"%data["summary"])
			fout.write("<tr>")
			self.datas.remove(data)
		fout.write("<table>")
		fout.write("<body>")
		fout.write("<html>")
		fout.close()

# 爬虫调度器
class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()

	def crawl(self, root_url):

		while (self.manager.is_or_not_new_url() and self.manager.done_urls_size() <100):
			try:
				new_url = self.manager.get_undo_url()
				html = self.downloader.download(new_url)
				new_urls, data = self.parser.parser(new_url, html)
				self.manager.add_urls_to_undo_urls(new_urls)
				self.output.store_data(data)
				print("已抓取%s个链接"%self.manager.undo_urls_size())
			except Exception as e:
				print("crawl failed!")
		self.output.output_html()

if __name__ == '__main__':
	spider_man = SpiderMan()
	spider_man.crawl("https://baike.baidu.com/view/284853.htm") #https://baike.baidu.com/view/10812319.htm