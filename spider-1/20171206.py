# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/6  15:38
# @abstract    :
'''
 1. beatifulsoup的find; beatifulsoup 的select；
 2、xpath;
 3、wb文件load的urllip.request.retrieve和write（py2的是urllip.retrieve）
 4、设置email提醒
'''

import requests
from bs4 import BeautifulSoup
import json,csv, re
import chardet
from lxml import etree

def getHtml(url):
	user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
	headers = {"User-Agent":user_agent}
	return requests.get(url, headers = headers)
# print(r.text)
# print(chardet.detect(r.content)) #{'encoding': 'utf-8', 'language': '', 'confidence': 0.99}
# r.encoding = chardet.detect(r.content)["encoding"] #检测网页编码，用该编码进行处理

# beatifulsoup的find; beatifulsoup 的select；xpath
def getContent(r):
	content = []
	soup = BeautifulSoup(r.text, "html.parser") #,from_encoding="utf-8"
	for mulu in soup.find_all(class_ = "mulu"):
		h2 = mulu.find("h2")
		if h2 !=None: #find找不到返回none，select则为空列表
			h2_title = h2.string #类似text
			# print(h2_title)
			list_urlAndname = []
			# for a in mulu.find(class_="box").find_all("a"): #可用列表推导式
			# 	href = a.get("href")
			# 	box_titlle = a.get("title")
			# 	# print(href, box_titlle)
			# 	list.append({"href":href, "box_title":box_titlle})
			list_urlAndname = [{"href":a.get("href"), "box_title":a.get("title")} for a in mulu.find(class_="box").find_all("a")]
			content.append({"title":h2_title, "content":list_urlAndname})
	# print(content)
	save_to_json(content)

def getContent_3(r):
	rows = []
	pattern = re.compile(r"\s*\[(.*)\]\s+(.*)")
	soup = BeautifulSoup(r.text, "html.parser") #html.parser,from_encoding="GBK"
	for mulu in soup.find_all(class_ = "mulu"):
		h2 = mulu.find("h2")
		if h2 !=None: #find找不到返回none，select则为空列表
			h2_title = h2.string #类似tex
			list = []
			for a in mulu.find(class_="box").find_all("a"): #可用列表推导式
				href = a.get("href")
				box_titlle = a.get("title")
				match = pattern.search(box_titlle)
				date = match.group(1)
				real_title = match.group(2)
				content = (h2_title, real_title, href, date)
				rows.append(content)
			# rows = [(h2_title, pattern.search(a.get("title")).group(2).encode("utf-8"), \
			# 		 a.get("href"), pattern.search(a.get("title")).group(2).encode("utf-8")) for a in mulu.find(class_="box").find_all("a")]
				# print(href, box_titlle)
	# print(rows)
	save_to_csv(rows)

def getContent_4(r):
	html = etree.HTML(r.text)
	div_mulus = html.xpath('.//*[@class="mulu"]')
	pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
	rows = []
	for div_mulu in div_mulus:
		div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
		if len(div_h2) > 0:
			h2_title = div_h2[0]
			a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
			for a in a_s:
				href = a.xpath('./@href')[0]
				box_title = a.xpath('./@title')[0]
				match = pattern.search(box_title)
				if match!= None:
					date = match.group(1)
					real_title = match.group(2)
					content = [h2_title, real_title, href, date]
					rows.append(content)
	print(rows)
	save_to_csv(rows)

def getContent_2(r):
	soup = BeautifulSoup(r.text, "lxml")
	for mulu in soup.select(".mulu"):
		h2 = mulu.select("h2")
		if h2:
			h2_title = h2[0].text
			print(h2_title)
			for a in mulu.select(".box")[0].select("a"):
				print(a, type(a))
				return
				href = a["href"]
				a_title = a["title"]
				print(href, a_title)

def save_to_csv(content):
	row_headers = ["title", "chapter-title", "href", "time" ]
	with open("D:/20160910/ruanjian/pycharmfile/spider_learn/spider-1/qiye.csv", "w") as f:
		f_csv = csv.writer(f)
		f_csv.writerow(row_headers)
		f_csv.writerows(content)
	print("end!")
	# with open("D:/20160910/ruanjian/pycharmfile/spider_learn/spider-1/qiye.csv", "r") as f:
	# 	f_csv = csv.reader(f)
	# 	headers = next(f_csv)
	# 	print(headers)
	# 	for row in f_csv:
	# 		print(row)

def save_to_json(content):
	with open("D:/20160910/ruanjian/pycharmfile/spider_learn/spider-1/qiye.json", "w") as fp:
		json.dump(content, fp = fp, indent= 4, ensure_ascii=False)
	with open("D:/20160910/ruanjian/pycharmfile/spider_learn/spider-1/qiye.json", "r") as fp:
		print(json.load(fp))

# r = getHtml("http://seputu.com/")

# getContent_2(r)
# getContent(r)
# getContent_3(r)
# getContent_4(r)

def img_to_load():
	import urllib,os
	def Schedule(blocknum, blocksize, totalsize):
		per = 100.0 * blocknum * blocksize / totalsize
		if per > 100:
			per = 100
			print("当前下载进度: %d"%per)
	req = getHtml("http://www.ivsky.com/tupian/ziranfengguang/")
	# html = etree.HTML(req.text)
	# img_urls = html.xpath(".//img/@src")
	# i = 0
	# for img_url in img_urls:
	# 	path = os.path.join("D:/d/spider/20171208","img{0}.jpg".format(i))
	# 	urllib.request.urlretrieve(img_url, path, Schedule)
	# 	i +=1
	soup = BeautifulSoup(req.text, "html.parser")
	ali = soup.select(".ali")
	pattern = re.compile(r'src="(.+\.jpg)"')
	for li in ali[0].select("li"):
		# print(li.select("a")[0])
		# match = pattern.search(str(li.select("a")[0]))
		# print(match.group(1))
		# print(li.select("a")[0]["title"])
		img_url = pattern.search(str(li.select("a")[0])).group(1)
		title = li.select("a")[0]["title"]
		path = os.path.join("D:/d/spider/20171208/write-method", "{0}.jpg".format(title))
		with open(path, "wb") as f:
			f.write(getHtml(img_url).content)

# img_to_load()

#email 提醒

def send_warn_to_email():
	from email.mime.text import MIMEText
	from email.header import Header
	from email.utils import parseaddr, formataddr
	import  smtplib

	def _format_addr(s):
		name, addr = parseaddr(s)
		return formataddr((Header(name, 'utf-8').encode(), addr))
	from_addr = "{}".format('13055415855@163.com')
	# password = 'hai878751686'
	password = 'hai!SHUI249114'
	to_addr = ",".join(['1467288927@qq.com'])
	smtp_server = 'smtp.163.com'
	try:
		msg = MIMEText('Python 爬虫运行异常，异常信息为遇到HTTP 403', "plain", "utf-8")
		msg['From'] = from_addr
		msg['To'] = to_addr
		msg['Subject'] = Header('一号爬虫运行状态 ', 'utf-8').encode()
		#发送邮件
		server = smtplib.SMTP_SSL(smtp_server, timeout=15)
		# server = smtplib.SMTP()
		# server.connect(smtp_server)
		server.login(from_addr, password)
		server.sendmail(from_addr, [to_addr], msg.as_string())
		server.quit()
	except Exception as e:
		print(e)

# send_warn_to_email()

def qq_smtp(message, subject, to_addr): #可以
	import smtplib
	from email.mime.text import MIMEText
	res = True
	try:
		msg = MIMEText(message, 'plain', 'utf-8')
		msg['From'] ='1467288927@qq.com'
		msg["To"] = ",".join(to_addr)
		msg['Subject'] =subject

		server = smtplib.SMTP_SSL("smtp.qq.com", 465)
		server.login('1467288927@qq.com', "dsgbgxqytfehgaed") #mdftqlacyiiegccf
		server.sendmail('1467288927@qq.com', to_addr, msg.as_string())
		server.quit()
	except Exception as e:
		print(e)
		res = False
	return res

# qq_smtp("你好!!!嗯", "smpt测试",["1467288927@qq.com","878751686@qq.com"])

import smtplib
import datetime
from email.mime.text import MIMEText

class emailSender(object):
    def __init__(self):
        self.smtp_host = "smtp.qq.com"      # 发送邮件的smtp服务器（从QQ邮箱中取得）
        self.smtp_user = "1467288927@qq.com" # 用于登录smtp服务器的用户名，也就是发送者的邮箱
        self.smtp_pwd = "dsgbgxqytfehgaed"  # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
        self.smtp_port = 465                # smtp服务器SSL端口号，默认是465
        self.sender = "1467288927@qq.com"    # 发送方的邮箱

    def sendEmail(self, toLst, subject, body):
        '''
        发送邮件
        :param toLst: 收件人的邮箱列表["465482631@qq.com", "77789713@qq.com"]
        :param subject: 邮件标题
        :param body: 邮件内容
        :return:
        '''
        message = MIMEText(body, 'plain', 'utf-8')  # 邮件内容，格式，编码
        message['From'] = self.sender               # 发件人
        message['To'] = ",".join(toLst)             # 收件人列表
        message['Subject'] = subject                # 邮件标题
        try:
            smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)   # 实例化一个SMTP_SSL对象
            loginRes = smtpSSLClient.login(self.smtp_user, self.smtp_pwd)      # 登录smtp服务器
            print("登录结果：loginRes = {0}".format(loginRes))    # loginRes = (235, b'Authentication successful')
            if loginRes and loginRes[0] == 235:
                print("登录成功，code = {loginRes[0]}")
                smtpSSLClient.sendmail(self.sender, toLst, message.as_string())
                print("mail has been send successfully. message:{message.as_string()}")
            else:
                print("登陆失败，code = {loginRes[0]}")
        except Exception as e:
            print("发送失败，Exception: e={0}".format(e))

# demo = emailSender()
# demo.sendEmail(["878751686@qq.com"], "smpt测试", "类测试你好！！！")

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '13055415855@163.com'
receiver = '1467288927@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '13055415855@163.com'
password = 'hai878751686'

msg = MIMEText('你好','text','utf-8') #中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()