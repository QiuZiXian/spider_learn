# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  20:25
# @abstract    :

import os

def get_the_path2(pathname):
    for filename in os.listdir(pathname):#该路径下的所有子目录和子文件
        print(filename)
    # print("-------------------------")
##    import glob
##    for file in glob.glob(filname):
##        print(file)
    print("-------------------------")
    for dirpath,dirnames,file in os.walk(pathname):
        # print(dirpath) # 所有目录名，包括自身及所有子目录
        # print("*******")
        for filename in file:
            print(filename)
        print("####")

get_the_path2("D:/d/spider/adult-movies")