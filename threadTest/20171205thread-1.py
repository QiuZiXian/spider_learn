# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/5  11:10
# @abstract    :

import numpy as np

# a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
# print(a)

# print( np.arange(0, 60, 10).reshape(-1, 1))

import random
import time,threading

def thread_run(urls):
	print("Current %s is running..." %threading.current_thread().name)
	for url in urls:
		print("%s--->>>%s"%(threading.current_thread().name, url))
		time.sleep(random.random())
	print("%s ended." %threading.current_thread().name)
print("Current %s is running..." %threading.current_thread().name)
t1 = threading.Thread(target=thread_run, name="Thread_1", args=(["url_1","url_2", "url_3"],))
t2 = threading.Thread(target=thread_run, name="Thread_2", args=(["url_4","url_5", "url_6"],))
# t3 = threading.Thread(target=thread_run(), name="Thread_1", args=["url_7","url_8", "url_9"])
t1.start()
t2.start()
t1.join()
t2.join()
print("%s ended." %threading.current_thread().name)