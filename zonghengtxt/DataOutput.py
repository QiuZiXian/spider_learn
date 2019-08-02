# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/9  11:35
# @abstract    :

#数据存储器
import time, os
import json, re

path = "D:/d/spider/zonghengtxt"
zhToNum = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10, "百": 100, "千": 1000}
class DataOutput(object):

	def __init__(self):
		self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
		self.datas = []

	def _handleTitle(self, title):
		try:
			oldTitle = re.match(r'第(.+?)章', title).group(1)
			titleZh = oldTitle.replace("零", "")
			# print(titleZh)
			qianIndex = titleZh.find("千")
			if qianIndex == -1:
				qian = "零"
			else:
				qian = titleZh[0]
			baiIndex = titleZh.find("百")
			if baiIndex == -1:
				bai = "零"
			else:
				bai = titleZh[baiIndex -1]
			shiIndex = titleZh.find("十")
			if shiIndex == -1:
				shi = "零"
			else:
				if titleZh[0] == "十":
					shi = "一"
				else:
					shi = titleZh[shiIndex - 1]
			# print(shiIndex, len(titleZh))
			if titleZh[-1] in ["十","百", "千"]:
				if titleZh[0] == "十": # 此时即title为“十”
					shi = "一"
				ge = "零"
			else:
				ge = titleZh[-1]
			# print(qian, bai, shi, ge)
			new_title = title.replace(oldTitle, str(int("{0}{1}{2}{3}".format(zhToNum[qian], zhToNum[bai], zhToNum[shi], zhToNum[ge]))))
			# print(new_title)
		except:
			new_title = title
		return new_title

	def dataToTxt(self,vol, title, readtxt):
		new_path = os.path.join(os.getcwd(), vol)
		if not os.path.isdir(new_path):
			os.mkdir(new_path)
		title = self._handleTitle(title) # 将中文章节转为数字章节
		filename = os.path.join(new_path, "{}.txt".format(title))
		with open(filename, "w", encoding="utf-8") as f:
			for line in readtxt:
				f.writelines("  {}".format(line))
				f.writelines("\n")

	def charpterToJson(self,tabtitle, ficName, data):
		path2 = os.path.join(path, tabtitle)
		if not os.path.isdir(path2):
			os.mkdir(path2)
		new_path = os.path.join(path2, ficName)
		if not os.path.isdir(new_path):
			os.mkdir(new_path)
		os.chdir(new_path)
		filename = os.path.join(new_path, "{}.json".format(ficName))
		with open(filename, "w") as fp:
			json.dump(data, fp = fp, indent= 4, ensure_ascii=False)

	def freeContToJson(self, ficName, data):
		new_path = os.path.join(path, ficName)
		if not os.path.isdir(new_path):
			os.mkdir(new_path)
		os.chdir(new_path)
		filename = os.path.join(new_path, "{}.json".format(ficName))
		with open(filename, "w") as fp:
			json.dump(data, fp = fp, indent= 4, ensure_ascii=False)

	def loadJson(self, ficName):
		new_path = os.path.join(path, ficName)
		if not os.path.isdir(new_path):
			os.mkdir(new_path)
		os.chdir(new_path)
		filename = os.path.join(new_path, "{}.json".format(ficName))
		with open(filename, "r") as fp:
				allChapter = json.load(fp)
		return allChapter

	def getLocalDoneFic(self):
		hasDoneFicList = []
		for dirpath, dirnames, file in os.walk(path):
			freeContDict =[ {"tabTitle": item, "tabLists": []} for item in dirnames if item != "免费小说首页"]
			break
		for item in freeContDict:
			for dirpath, dirnames, file in os.walk(os.path.join(path, item["tabTitle"])):
				item["tabLists"] = [item.lstrip("0123456789") for item in dirnames]
				for List in dirnames:
					hasDoneFicList.append(List.strip("0123456789"))
				break
		return freeContDict, hasDoneFicList
		# return hasDoneFic
