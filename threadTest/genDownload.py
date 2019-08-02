# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  21:34
# @abstract    :

import os, csv, multiprocessing, shutil, time
import urllib.request

def downloadFilms(title, fileDownloadUrl, downloadPath):
	print("%s--正在下载..."%title)
	def Schedule( a,b,c):
		'''''
		a:已经下载的数据块
		b:数据块的大小
		c:远程文件的大小
	   '''
		per = 100.0 * a * b / c
		if per > 100 :
			per = 100
		# per_num = 1
		# if per//10 == per_num:
		# print ('%.2f%%' % per)
			# per_num += 1
	filename = os.path.join(downloadPath, "{0}.mp4".format(title))
	try:
		urllib.request.urlretrieve(fileDownloadUrl, filename, Schedule)
		print("%s--下载完毕..."%title)
	except:
		# print("%s--网络问题..."%title)
		pass


def readcsv(pathname, indexNum, indexMax):
	with open(pathname, "r") as fcsv:
		# print(len(fcsv.readlines())) # 获取文件最大行数
		reader = csv.reader(fcsv)
		for i, rows in enumerate(reader):
			if i <= indexMax:
				if i == indexNum:
					return rows
			else:
				return None

def getPath():
	# # 获取csv文件
	path = "D:/d/spider/adult-movies"
	path_backup = os.path.join(path, "backup")
	path_csv = os.path.join(path, "data")
	if os.path.isdir(path_backup):
		if os.path.isdir(path_csv):
			shutil.rmtree(path_csv)
		shutil.copytree(path_backup, path_csv)

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
	filepaths = [(os.path.join(path_csv, "{}.csv".format(file)), os.path.join(new_path, file), file) for file in new_files]
	# print(filepaths)
	# print(os.getcwd())
	return filepaths

def savePro(num, pathname):
	path = "D:/d/spider/adult-movies"
	new_path = os.path.join(path, "backup")
	if not os.path.isdir(new_path):
		os.mkdir(new_path)
	os.chdir(new_path)
	with open(pathname[0], "r") as fcsv:
		reader = csv.reader(fcsv)
		rows = [row for row in reader if row][num:]
		with open("{}.csv".format(pathname[2]), "w") as f:
			writer = csv.writer(f)
			writer.writerows(rows)

def download_1(pathname, Break):
	remain = True
	for i in range(3):
		filmNameAndDownloadUrl = readcsv(pathname[0], 2 * i, 100)
		if filmNameAndDownloadUrl:
			downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])
			if Break:
				return savePro(2 * i, pathname)
		else:
			remain = False
			break
	if remain:
		savePro(4, pathname)

def download_2(pathname, Break):
	remain = True
	for i in range(3):
		filmNameAndDownloadUrl = readcsv(pathname[0], 2 * i, 100)
		if filmNameAndDownloadUrl:
			downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])
			if Break:
				return savePro(2 * i, pathname)
		else:
			remain = False
			break
	if remain:
		savePro(4, pathname)

def download_3(pathname, Break):
	remain = True
	for i in range(3):
		filmNameAndDownloadUrl = readcsv(pathname[0], 2 * i, 100)
		if filmNameAndDownloadUrl:
			downloadFilms(filmNameAndDownloadUrl[0], filmNameAndDownloadUrl[1], pathname[1])
			if Break:
				return savePro(2 * i, pathname)
		else:
			remain = False
			break
	if remain:
		savePro(4, pathname)

def proMain(Break):
	pathnames = getPath()
	while pathnames:
		ps = []
		if pathnames:
			p1 = multiprocessing.Process(target=download_1, args=(pathnames.pop(), Break))
			ps.append(p1)
			# if pathnames:
			# 	# pathname = pathnames.pop()
			# 	p2 = multiprocessing.Process(target=download_2, args=(pathnames.pop(), Break))
			# 	ps.append(p2)
			# 	if pathnames:
			# 		# pathname = pathnames.pop()
			# 		p3 = multiprocessing.Process(target=download_3, args=(pathnames.pop(), Break))
			# 		ps.append(p3)
		else:
			break
		if ps:
			for p in ps:
				p.daemon = True
				p.start()
			for p in ps:
				p.join()
		print(len(ps))

if __name__ == '__main__':
	# startt = time.time()
	# downloadFilms("test3", "https://d1.xia12345.com/down/201611/30/cjk6.mp4","D:/d/spider/adult-movies")
	# proMain(Break=False)
	# endt = time.time()
	# print("本次爬虫共耗时%s,合%s分钟"%((endt - startt), (endt - startt)/60))
	downUrl = "https://d1.xia12345.com/201607/30/bdyjy139.mp4"
	os.execl(r"D:\影音\Program\Thunder.exe",DesktopIcon %downUrl)