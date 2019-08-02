# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  21:34
# @abstract    :

import os, csv, multiprocessing
import urllib

class genDownload(object):

	def downloadFilms(self, title, fileDownloadUrl, downloadPath):
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
		urllib.request.urlretrieve(fileDownloadUrl, filename, Schedule)

	def readcsv(self, pathname, indexNum, indexMax):
		with open(pathname, "r") as fcsv:
			# print(len(fcsv.readlines())) # 获取文件最大行数
			reader = csv.reader(fcsv)
			for i, rows in enumerate(reader):
				if i <= indexMax:
					if i == indexNum:
						return rows

	def getPath(self):
		# # 获取csv文件
		path = "D:/d/spider/adult-movies"
		path_csv = os.path.join(path, "data")
		#csv文件处理
		new_files = [item.split(".")[0] for item in [file for dirpath, dirnames, file in os.walk(path_csv)][0]]
		# print(new_files)
		# csvToload = {}
		os.chdir(path)
		new_path = os.path.join(path, "download")
		if os.path.exists(new_path):
			os.chdir(new_path)
		else:
			os.mkdir("download")
			os.chdir(new_path)
		# 创建文件夹
		new_dirs = [os.path.join(path, dirname) for dirname in new_files]
		for filename in new_files:
			if os.path.isdir(filename):
				pass
			else:
				os.mkdir(filename)
		filepaths = [(os.path.join(path_csv, "{}.csv".format(file)), os.path.join(new_path, file)) for file in new_files]
		# print(filepaths)
		# print(os.getcwd())
		return filepaths

	def download_1(self, pathname):
		for i in range(10):
			filmNameAndDownloadUrl = self.readcsv(pathname[0], 2 * i, 100)
			self.downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])

	# def download_2(self, pathname):
	# 	for i in range(10):
	# 		filmNameAndDownloadUrl = readcsv(pathname[0], 2 * i, 100)
	# 		downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])
	#
	# def download_3(self, pathname):
	# 	for i in range(10):
	# 		filmNameAndDownloadUrl = readcsv(pathname[0], 2 * i, 100)
	# 		downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])

# def proMain():
# 	pathname = getPath()
# 	p1 = multiprocessing.Process(target=download_1, args=(pathname[0],))
# 	p2 = multiprocessing.Process(target=download_2, args=(pathname[1],))
# 	p3 = multiprocessing.Process(target=download_3, args=(pathname[2],))
# 	ps = [p1, p2, p3]
# 	for p in ps:
# 		p.daemon = True
# 		p.start()
# 	for p in ps:
# 		p.join()

if __name__ == '__main__':
	demo = genDownload()
	demo.downloadFilms("test3", "https://d1.xia12345.com/down/201704/30/ydgzy19.mp4","D:/d/spider/adult-movies")
    # proMain()
