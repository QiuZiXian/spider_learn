# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/22  21:18
# @abstract    :

from lol_laoyuegou_spider.HtmlDownloader import HtmlDownloader
from bs4 import BeautifulSoup
import re, csv

url = "http://www.laoyuegou.com/x/zh-cn/lol/lol/godrank.html?region=cn"

headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
temp = ['卡拉曼达', '均衡教派', '守望之海', '巨神峰', '影流', '征服之海', '战争学院', '暗影岛', '比尔吉沃特', '水晶之痕', '班德尔城', '皮城警备', '皮尔特沃夫', '祖安', '艾欧尼亚', '裁决之地', '诺克萨斯', '钢铁烈阳', '雷瑟守备', '黑色玫瑰']
downloader = HtmlDownloader()

def getSeverCon(url):
	response =downloader.download(url)
	soup = BeautifulSoup(response, "html.parser")
	servers = soup.select(".select")
	# print(servers[-1])
	# serverCon = []
	# for item in servers[-1].select('a'):
	# 	serverCon.append({"href": item["href"], "serverName":  item.text})
	serverCon = [{"href": item["href"], "serverName":  item.text.strip("\n\t")} for item in servers[-1].select('a')]
	return serverCon

def getRowCon(soup):
	pageCon = []
	for item in soup.select(".row"):
		rowCon = []
		rowCon.append(item.select(".item1")[0].text) # 排名
		rowCon.append("None") # 国服id受隐私保护
		rowCon.append(item.select(".item3")[0].text.strip("\n")) # 段位，胜点
		#胜场，负场， 胜率
		try:
			yAndN = item.select(".item4")[0].select("span")
			y = yAndN[0].text # 胜场
			n = yAndN[-2].text # 负场
			yn = yAndN[-1].text # 胜率
		except:
			y, n, yn = "None", "None", "None"
		rowCon.append(y)
		rowCon.append(n)
		rowCon.append(yn)
		recentState = re.search(r"/img/score/(.+?)\.png", str(item.select(".item5")[0])).group(1)
		rowCon.append(recentState)
		bestPos = item.select(".item6 > .color-zhongdan")[0].text
		rowCon.append(bestPos)
		try:
			bestRole = re.findall(r'alt="(.+?)"', str(item.select(".item7")[0]))
			rowCon.append(','.join(bestRole))
		except:
			rowCon.append("None")
		pageCon.append(rowCon)
	return pageCon

def getCont(url, catagory):
	allPageCon  = []

	for page in range(1, 11):
		new_url = "{}&page={}".format(url, page)
		response = downloader.download(new_url)
		soup = BeautifulSoup(response, "html.parser")
		allPageCon.append(getRowCon(soup))
		nextPage = soup.select(".pagination")[0].select('a')
		if page !=1 and len(nextPage) == 1:
			break
	# catagory = "德玛西亚"
	csvHeaders = ["排名", "玩家", "段位/胜点", "胜场", "负场", "胜率", "最近状态", "擅长位置", "本命英雄"]
	with open("D:/d/spider/laoyuegouLOL/data/{0}.csv".format(catagory), "a") as fcsv:
		csvwriter = csv.writer(fcsv)
		csvwriter.writerow(csvHeaders)
		for pageCon in allPageCon:
			csvwriter.writerows(pageCon)
	print("{}, end!".format(catagory))

# print(getSeverCon(url))
for item in getSeverCon(url):
	if item["serverName"] in temp:
		continue
	getCont(item["href"], item["serverName"])
print("all end!!")