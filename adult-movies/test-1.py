# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/26  20:08
# @abstract    :

import requests
from bs4 import BeautifulSoup
import re
from urllib import parse
import urllib, os, csv

class AdultFilm():

	def __init__(self):
		self.film_links = {}

	def downloadHtml(self, url):
		if url is None:
			return None
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
		headers = {"User-Agent":user_agent}
		r = requests.get(url, headers = headers)
		if r.status_code == 200:
			r.encoding = "utf-8" #可引入chardet检测编码进行优化r.encoding = chardet.detect(r.content)["encoding"]
			return r.text
		return None

	def parse(self, root_url, html_cont):
		# 根页面处理
		# soup = BeautifulSoup(html_cont, "html.parser") # , from_encoding="utf-8"
		# ul = soup.find_all('a', href = re.compile(r'Html/.+\.html'))
		titleAndlinks = {}
		# titleAndlinks["网站首页"] = [[(li.text, parse.urljoin(root_url, li['href'])) for li in ul]]
		# titles_2 = [li.text for li in ul]
		# print(links, titles_2)
		# print(len(links), len(titles_2))
		#获取大分类
		# catagory_urls = self._getcatagory_urls(root_url)
		catagory_urls = [('苍井空', 'https://www.1557v.com/Html/96/'), ('宇都宮紫苑', 'https://www.1557v.com/Html/128/')]
		#每个分类下的所有页码地址
		catagoryAndpages_dict = self._getpage_urls(catagory_urls)
		# page_urls = ["https://www.1553v.com/Html/94/"]
		#每一页所有film的film标题和网址
		for catagory, page_urls in catagoryAndpages_dict.items():
			for page_url in page_urls:
				try:
					new_html = self.downloadHtml(page_url)
					new_soup = BeautifulSoup(new_html, "html.parser")
					ul = new_soup.find("div", class_="box movie_list").find("ul").find_all('a', href = re.compile(r'Html/.+\.html'))
					if catagory in titleAndlinks:
						titleAndlinks[catagory].append([(li.text, parse.urljoin(root_url, li['href'])) for li in ul])
					else:
						titleAndlinks[catagory] = [[(li.text, parse.urljoin(root_url, li['href'])) for li in ul]]
				except:
					pass

				#获取下载链接
		for catagory, links in titleAndlinks.items():
			self._getfilm_urls(catagory, links)
		print("begin save!")
		self.dataTocsv()

	def _getfilm_urls(self, catagory, links):
		self.film_links[catagory] = []
		for item in links:
			for filmName, link in item:
				new_html = self.downloadHtml(link)
				new_soup = BeautifulSoup(new_html, "html.parser")
				try:
					self.film_links[catagory].append((filmName, new_soup.find("ul", class_='downurl').find('a')['href']))
				except:
					continue
			# print(self.film_links)

	def _getpage_urls(self, catagory_urls):
		link = "https://www.1553v.com/Html/94/"
		catagoryAndpages_dict = {}
		for catagory, link in catagory_urls:
			new_html = self.downloadHtml(link)
			new_soup = BeautifulSoup(new_html, "html.parser")
			page_end = new_soup.find('div', class_="pagination").find_all('a')[-1]['href']
			# page_end = '/Html/94/index-11.html'
			page_end_num = int(re.findall("index-(\d+?)\.html", page_end)[0])
			catagoryAndpages_dict[catagory] = ["{0}index-{1}.html".format(link, num) for num in range(2, page_end_num +1)]
			catagoryAndpages_dict[catagory].append("{0}index.html".format(link) )
		# print(page_urls, len(page_urls))
		return catagoryAndpages_dict

	def _getcatagory_urls(self, root_url):
		from selenium import webdriver
		url = "https://www.1551v.com"
		browser = webdriver.Firefox()
		browser.implicitly_wait(10)
		browser.get(root_url)
		div = browser.find_elements_by_class_name("nav_menu")
		# print(div)
		nav = []
		for lu in div:
			lis = lu.find_elements_by_tag_name('li')
			for li in lis:
				try:
					nav.append((li.text, li.find_element_by_tag_name('a').get_attribute('href')))
				except:
					pass
		catagory_urls = [(title, link) for title, link in nav if link[-2].isdigit()]
		return catagory_urls

	def dataTocsv(self):
		with open("D:/d/spider/adult-movies/data/seed.csv", "w") as fcsv:
			csvwriter = csv.writer(fcsv)
			for title, titleAndlink in self.film_links.items():
				csvwriter.writerow([title])
				csvwriter.writerows(titleAndlink)
		print("write end!")

	def downloadFilms(self, title, new_url):
		def Schedule( a,b,c):
			'''''
			a:已经下载的数据块
			b:数据块的大小
			c:远程文件的大小
		   '''
			per = 100.0 * a * b / c
			if per > 100 :
				per = 100
			# if per/10
			print ('%.2f%%' % per)
		filename = os.path.join("D:/d/spider/adult-movies", "{0}.mp4".format(title))
		urllib.request.urlretrieve(new_url, filename, Schedule)

if __name__ == '__main__':
	url = "https://www.1551v.com"
	demo = AdultFilm()
	# html_cont = demo.downloadHtml(url)
	# demo.parse(url, html_cont)
	# demo.downloadFilms("test2", "https://d1.xia12345.com/down/201704/30/ydgzy19.mp4")
	# print(demo.downloadHtml("https://www.1733v.com/Html/84/12319.html"))
	cont = demo.downloadHtml("https://www.1733v.com/Html/84/12319.html")
	print(re.search(r'<font size="4" color="#1e1d1d">(.+?)</font></div>', cont, re.S).group(1).replace("<br><br>", "\n"))