# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  20:41
# @abstract    :

import os, csv

def getPath(pathname):
	for dirpath, dirnames, file in os.walk(pathname):
		# print(dirpath) # 从当前路径开始，返回文件夹路径名
		# print(dirnames) #从当前路径开始，每一级目录下的文件名，以列表返回，直到子目录下无文件夹，返回空列表
		print(file)
		return file
temp = [item.split(".")[0] for item in getPath("D:/d/spider/laoyuegouLOL/data")]
print(temp)
# getPath("D:/d/spider/zonghengtxt")
# getPath("D:/d/spider/adult-movies/data")
# # 获取csv文件
path = "D:/d/spider/adult-movies"
path_csv = os.path.join(path, "data")
#csv文件处理
# new_files = [item.split(".")[0] for item in [file for dirpath, dirnames, file in os.walk(path_csv)][0]]
# print(new_files)
# csvToload = {}
# os.chdir(path)
# new_path = os.path.join(path, "download")
# if os.path.exists(new_path):
# 	os.chdir(new_path)
# else:
# 	os.mkdir("download")
# 	os.chdir(new_path)
# # 创建文件夹
# new_dirs = [os.path.join(path, dirname) for dirname in new_files]
# for filename in new_files:
# 	if os.path.isdir(filename):
# 		pass
# 	else:
# 		os.mkdir(filename)
# filepaths = [(os.path.join(path_csv, "{}.csv".format(file)), os.path.join(new_path, file)) for file in new_files]
# print(filepaths)
# print(os.getcwd())

# # 获取第indexNum行数据
# def readcsv(pathname, indexNum, indexMax):
# 	with open(pathname, "r") as fcsv:
# 		# print(len(fcsv.readlines())) # 获取文件最大行数
# 		reader = csv.reader(fcsv)
# 		for i, rows in enumerate(reader):
# 			if i <= indexMax:
# 				if i == indexNum:
# 					return rows
#
# pathname = "D:/d/spider/adult-movies/data/天海翼.csv"
# # for i in range(0,10, 2):
# # 	print(readcsv(pathname, i, 20))
# # readcsv(pathname, 2, 20)
# with open(pathname, "r") as fcsv:
# 	reader = csv.reader(fcsv)
# 	rows = [row for row in reader if row]
# 	with open("D:/d/spider/adult-movies/data/test.csv", "w") as f:
# 		writer = csv.writer(f)
# 		writer.writerows(rows)
# 	print("end")