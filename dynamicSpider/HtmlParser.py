# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/13  19:16
# @abstract    :

import re
import json
from dynamicSpider.DataOutput_2 import DataOutput_2

class HtmlParser(object):

	def parser_url(self, page_url, response):
		pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
		urls = pattern.findall(response)
		if urls != None:
			return list(set(urls)) #去重
		else:
			return None

	def parser_json(self, page_url, response):
		pattern = re.compile(r'=(.*?);')
		result = pattern.findall(response)[0]
		if result != None:
			value = json.loads(result)
			# print(value)
			try:
				isRelease = value.get('value').get('isRelease')
				# print(isRelease)
				# return
			except Exception as e:
				print(e)
				return None
			if isRelease: # isRelease 值：已上映电影未true，未上映为false
				if value.get('value').get('hotValue') == None:
					# print("**")
					return self._parser_release(page_url, value)
				else:
					return self._paser_no_release(page_url,value, isRelease=2)
			else:
				return self._paser_no_release(page_url,value)


	def _parser_release(self, page_url, value): #解析已上映电影
		try:
			isRelease = 1
			movieTitle = value.get('value').get('movieTitle')

			movieRating = value.get('value').get('movieRating')
			RPictureFinal = movieRating.get('RPictureFinal')
			RStoryFinal = movieRating.get('RStoryFinal')
			RDirectorFinal = movieRating.get('RDirectorFinal')
			ROtherFinal = movieRating.get('ROtherFinal')
			RatingFinal = movieRating.get('RatingFinal')
			MovieId = movieRating.get('MovieId')
			Usercount = movieRating.get('Usercount')
			AttitudeCount = movieRating.get('AttitudeCount')

			boxOffice = value.get('value').get('boxOffice') # 票房信息，部分电影无此项
			TotalBoxOffice = boxOffice.get('TotalBoxOffice')
			TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
			TodayBoxOffice = boxOffice.get('TodayBoxOffice')
			TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
			ShowDays = boxOffice.get('ShowDays')
			try:
				Rank = boxOffice.get('Rank')
			except Exception as e:
				Rank = 0
			# print(MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal,\
			# 		Usercount, AttitudeCount, TotalBoxOffice + TotalBoxOfficeUnit, TodayBoxOffice + TodayBoxOfficeUnit, Rank, ShowDays, isRelease)
			return (MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal,\
					Usercount, AttitudeCount, TotalBoxOffice + TotalBoxOfficeUnit, TodayBoxOffice + TodayBoxOfficeUnit, Rank, ShowDays, isRelease)
		except Exception as e:
			# print(isRelease, e, page_url, value)
			return (isRelease, e, page_url, value) # None

	def _paser_no_release(self, page_url, value, isRelease = 0): # 解析未上映电影信息
		try:
			movieRating = value.get('value').get('movieRating')
			movieTitle = value.get('value').get('movieTitle')

			RPictureFinal = movieRating.get('RPictureFinal')
			RStoryFinal = movieRating.get('RStoryFinal')
			RDirectorFinal = movieRating.get('RDirectorFinal')
			ROtherFinal = movieRating.get('ROtherFinal')
			RatingFinal = movieRating.get('RatingFinal')
			MovieId = movieRating.get('MovieId')
			Usercount = movieRating.get('Usercount')
			AttitudeCount = movieRating.get('AttitudeCount')
			try:
				Rank = value.get('value').get('hotValue').get('Ranking')
			except Exception as e:
				Rank = 0
			return (MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal, Usercount, AttitudeCount, '无', '无', Rank, 0, isRelease)
		except Exception as e:
			# print(e, page_url, value)
			return (isRelease, e, page_url, value) # None