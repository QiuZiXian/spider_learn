# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  19:06
# @abstract    :

import random
import threading, time

def test(th):
	th.join()
	def subThread_run(urls):
		print("Current %s is running..." %threading.current_thread().name)
		for url in urls:
			print("%s--->>>%s"%(threading.current_thread().name, url))
			time.sleep(random.random())
		print("%s ended." %threading.current_thread().name)
	print("Current %s is running..." %threading.current_thread().name)
	t1 = threading.Thread(target=subThread_run, name="Thread_1", args=(["url_1","url_2", "url_3"],))
	t2 = threading.Thread(target=subThread_run, name="Thread_2", args=(["url_4","url_5", "url_6"],))
	# t3 = threading.Thread(target=thread_run(), name="Thread_1", args=["url_7","url_8", "url_9"])
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("%s ended." %threading.current_thread().name)

def mainThread_run():
	def first():
		pass
	th1 = threading.Thread(target=first)
	th1.start()
	th1 = threading.Thread(target=test, name="Thread_3", args=(th1,))
	th1.start() # 线程嵌套，其实和顺序执行一样。真正异步需要用进程

	th2 = threading.Thread(target=test, name="Thread_4",  args=(th1,))
	# t3 = threading.Thread(target=thread_run(), name="Thread_1", args=["url_7","url_8", "url_9"])
	th2.start()
	th2.join()
	print("%s ended." %threading.current_thread().name)

mainThread_run()