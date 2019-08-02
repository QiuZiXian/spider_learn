# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/1  19:53
# @abstract    :

import re
with open("D:/d/spider/zonghengtxt/biaoti.txt", "r", encoding="utf-8") as f:
	# print(f.readline())
	data = [line for line in f.readlines()]
# print(data)
zhToNum = {"零": '0', "一": '1', "二": '2', "三": '3', "四": '4', "五": '5', "六": '6', "七": '7', "八": '8', "九": '9', "十": '10', "百": '0', "千": '00'}
zhToNum_list = ['一',  '四', '八', '三',  '六', '七', '二', '十', '五', '九']
# print("|".join(zhToNum_list))
zhSplit = {"十": '10', "百": '0', "千": '00'}
zhNumSplit = ["十","百", "千"]
# print(data)
# print(zhToNum["千"])
# titles = re.findall(r'第.+?章', data[0])
titleNum = [ '七', '十', '十一', '二十', '二十一', '一百', '二百零一', '二百一十', '二百三十四', '九千', '九千零六',
			 '九千零一十', '九千五百', '九千八百零六', '九千八百七十六']
titles = ["第七章", "第十章", "第十一章", "第十七章", "第二十章", "第二十一章", "第一百章", "第二百零一章", "第二百一十章", "第二百三十四章",
		  "第九千章", "第九千零六章", "第九千零一十章", "第九千五百章", "第九千八百零六章", "第九千八百七十六章"]
for title in titles:
	oldTitle = re.match(r'第(.+?)章', title).group(1)
	titleZh = oldTitle.replace("零", "")
	# titleNum.append(oldTitle)
	print(oldTitle)
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
		if titleZh[0] == "十":  # 这里显然ge位也确定了，但下面只是覆盖了而已
			shi = "一"
		else:
			shi = titleZh[shiIndex - 1]
	# print(shiIndex, len(titleZh))
	if titleZh[-1] in ["十","百", "千"]: # 解决特殊值，整千整百
		if titleZh[0] == "十": # 解决特殊值 十
			shi = "一"
		ge = "零"
	else:
		ge = titleZh[-1]
	print(qian, bai, shi, ge)

	new_title = title.replace(oldTitle, str(int("{0}{1}{2}{3}".format(zhToNum[qian], zhToNum[bai], zhToNum[shi], zhToNum[ge]))))
	print(new_title)
print(titleNum)



