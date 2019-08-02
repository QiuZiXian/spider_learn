# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/11  19:30
# @abstract    :

from secondSpider.UrlManger import UrlManager
from secondSpider.DataOutput import DataOutput
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import Queue
import time

class NodeManager(object):

	def start_Manager(self, url_q, result_q):
		BaseManager.register('get_task_queue', callable = lambda :url_q)
		BaseManager.register('get_result_queue', callable = lambda :result_q)
		manager = BaseManager(addree = ('', 8001), authkey = 'baike')
		return manager

	def url_manager_proc(self, url_q, conn_q, root_url):
		url_manager = UrlManager()
		url_manager.add_url_to_undo_urls(root_url)
		while True:
			while (url_manager.is_or_not_new_url()):
				new_url = url_manager.get_undo_url()
				url_q.put(new_url)
				print('done_url = ', url_manager.done_urls_size())
				if (url_manager.done_urls_size() >2000):
					url_q.put("end")
					print("控制点发出结束通知！")
					url_manager.save_progress('D:/d/spider/20171211/undo_urls.txt', url_manager.undo_urls)
					url_manager.save_progress('D:/d/spider/20171211/done_urls.txt', url_manager.done_urls)
					return
			try:
				if not conn_q.empty():
					urls = conn_q.get()
					url_manager.add_urls_to_undo_urls(urls)
			except BaseException as e:
				time.sleep(0.1)

	def store_proc(self, store_q):
		output = DataOutput()
		while True:
			if not store_q.empty():
				data = store_q.get()
				if data == 'end':
					print('存储进程已接受')
					output.output_end()

					return
				output.store_data(data)
			else:
				time.sleep(0.1)

if __name__ == '__main__':
	url_q = Queue()
	result_q = Queue()
	store_q = Queue()
	conn_q = Queue()
	node = NodeManager()
	manager = node.start_Manager(url_q, result_q)
	url_manager_proc = Process(target = node.url_manager_proc, args = (url_q, conn_q, 'http://baike.baidu.com/view/284853.htm'))
	result_solve_proc = Process(target=node.result_solve_proc, args= (result_q, conn_q, store_q))
	store_proc = Process(target=node.store_proc, args=(store_q,))

	url_manager_proc.start()
	result_solve_proc.start()
	store_proc.start()
	manager.get_server().serve_forever()

