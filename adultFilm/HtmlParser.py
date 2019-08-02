# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:37
# @abstract    :

#HTML解析器
import re
from urllib import parse
from bs4 import BeautifulSoup
from adultFilm.HtmlDownloader import HtmlDownloader
from adultFilm.UrlManger import UrlManager
import threading

# film_links = [] # 不会用？？？
L = threading.Lock()

class HtmlParser(object):

	def __init__(self):
		self.downloader = HtmlDownloader()
		self.manager = UrlManager()
		self.film_links = []

	def parser(self, root_url, html_cont):
		if root_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont, "html.parser")
		ul = soup.find_all('a', href = re.compile(r'Html/.+\.html'))
		titleAndlinks = {}
		# titleAndlinks["网站首页"] = [(li.text, li['href']) for li in ul]
		# self.manager.add_urls_to_undo_urls([link for title, link in titleAndlinks["网站首页"][0]])
		# catagory_urls = self._getcatagory_urls(root_url)
		# print(catagory_urls)
		# catagory_urls = [('国产精品', 'https://www.1577v.com/Html/60/'), ('亚洲无码', 'https://www.1577v.com/Html/110/'), ('欧美性爱', 'https://www.1577v.com/Html/62/'), ('VR虚拟现实', 'https://www.1577v.com/Html/86/'), ('成人动漫', 'https://www.1577v.com/Html/101/'), ('自拍图片', 'https://www.1577v.com/Html/63/'), ('情色小说', 'https://www.1577v.com/Html/84/'), ('自拍偷拍', 'https://www.1577v.com/Html/89/'), ('夫妻同房', 'https://www.1577v.com/Html/87/'), ('开放90后', 'https://www.1577v.com/Html/93/'), ('换妻游戏', 'https://www.1577v.com/Html/90/'), ('网红主播', 'https://www.1577v.com/Html/91/'), ('手机小视频', 'https://www.1577v.com/Html/88/'), ('明星艳照门', 'https://www.1577v.com/Html/92/'), ('经典三级', 'https://www.1577v.com/Html/109/'), ('S级女优', 'https://www.1577v.com/Html/100/'), ('波多野结衣', 'https://www.1577v.com/Html/94/'), ('吉泽明步', 'https://www.1577v.com/Html/95/'), ('苍井空', 'https://www.1577v.com/Html/96/'), ('宇都宮紫苑', 'https://www.1577v.com/Html/128/'), ('天海翼', 'https://www.1577v.com/Html/98/'), ('水菜麗', 'https://www.1577v.com/Html/127/'), ('泷泽萝拉', 'https://www.1577v.com/Html/123/'), ('无码在线', 'https://www.1577v.com/Html/110/'), ('熟女人妻', 'https://www.1577v.com/Html/111/'), ('美颜巨乳', 'https://www.1577v.com/Html/112/'), ('颜射吃精', 'https://www.1577v.com/Html/113/'), ('丝袜制服', 'https://www.1577v.com/Html/114/'), ('高清无码', 'https://www.1577v.com/Html/130/'), ('中字有码', 'https://www.1577v.com/Html/131/')]
		# catagory_urls = [('宇都宮紫苑', "https://www.1575v.com/Html/128/"), ('泷泽萝拉', 'https://www.1575v.com/Html/123/')]
		catagory_urls = [ ('情色小说', 'https://www.1577v.com/Html/84/')] # ('自拍图片', 'https://www.1577v.com/Html/63/'),
		#每个分类下的所有页码地址
		catagoryAndpages_dict = self._getpage_urls(catagory_urls)
		catagory_list = [catagory for catagory in catagoryAndpages_dict.keys()]
		# page_urls = ["https://www.1553v.com/Html/94/"]
		return catagoryAndpages_dict, titleAndlinks,catagory_list

			#每一页所有film的film标题和网址
	def _getFilm_urls(self, new_html):
		try:
			new_soup = BeautifulSoup(new_html, "html.parser")
			ul = new_soup.find("div", class_="box movie_list").find("ul").find_all('a', href = re.compile(r'Html/.+\.html'))
			return [(li.text, li['href']) for li in ul]
		except:
			try:
				new_soup = BeautifulSoup(new_html, "html.parser")
				ul = new_soup.find("div", class_="box list channel").find("ul").find_all('a', href = re.compile(r'Html/.+\.html'))
				return [(li.text, li['href']) for li in ul]
			except:
				return None

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
		browser.close()
		catagory_urls = [(title, link) for title, link in nav if link[-2].isdigit()]
		print(catagory_urls)
		return catagory_urls

	def _getpage_urls(self, catagory_urls):
		# link = "https://www.1553v.com/Html/94/"
		catagoryAndpages_dict = {}
		for catagory, link in catagory_urls:
			new_html = self.downloader.download(link)
			if new_html:
				new_soup = BeautifulSoup(new_html, "html.parser")
				page_end = new_soup.find('div', class_="pagination").find_all('a')[-1]['href']
				# page_end = '/Html/94/index-11.html'
				page_end_num = int(re.findall("index-(\d+?)\.html", page_end)[0])
				catagoryAndpages_dict[catagory] = ["{0}index-{1}.html".format(link, num) for num in range(2, 4)] #page_end_num +1
				catagoryAndpages_dict[catagory].append("{0}index.html".format(link) )
			# print(page_urls, len(page_urls))
		return catagoryAndpages_dict

	def _getfilmdown_urls(self, root_url, nameAndLink):
		# film_links = [] #???
		self.film_links = [] # 用全局变量film_links不行？？最后返回仍为空？
		while nameAndLink:
			threads = []
			L.acquire()
			for i in range(5):
				if nameAndLink:
					filmName,link = nameAndLink.pop()
					t = threading.Thread(target=self._threadGetFilmDownUrl,name="{}".format(i), args=(root_url, filmName, link))
					threads.append(t)
				else:
					break
			L.release()
			if threads:
				for t in threads:
					t.start()
				for t in threads:
					t.join()
		print(self.film_links)
		return self.film_links

	def _getPictureOrFiction(self, root_url, nameAndLink):
		self.film_links = []
		while nameAndLink:
			threads = []
			L.acquire()
			for i in range(10):
				if nameAndLink:
					PicOrFic, link = nameAndLink.pop()
					t = threading.Thread(target=self._threadGetPicOrFic, name="{}".format(i), args=(root_url, PicOrFic, link))
					threads.append(t)
				else:
					break
			L.release()
			if threads:
				for t in threads:
					t.start()
				for t in threads:
					t.join()
		return self.film_links

	def _threadGetFilmDownUrl(self,root_url, filmName, link):
		new_html = self.downloader.download(parse.urljoin(root_url, link))
		new_soup = BeautifulSoup(new_html, "html.parser")
		try:
			self.film_links.append((filmName, new_soup.find("ul", class_='downurl').find('a')['href']))
		except:
			pass
		print(threading.current_thread().name, len(self.film_links))

	def _threadGetPicOrFic(self, root_url, PicOrFic, link):
		new_url = parse.urljoin(root_url, link)
		self.film_links.append((PicOrFic, new_url))

	def getFic(self, new_html):
		cont = re.search(r'<font size="4" color="#1e1d1d">(.+?)</font></div>', new_html, re.S).group(1).replace("<br><br>", "\n")
		return cont
if __name__ == '__main__':
	demo = HtmlParser()
	demo._getcatagory_urls("https://www.1551v.com")