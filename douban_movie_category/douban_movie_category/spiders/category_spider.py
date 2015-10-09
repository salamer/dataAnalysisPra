# -*- coding: utf-8 -*-
#encoding:utf-8

from scrapy.spiders import Spider 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from douban_movie_category.items import DoubanMovieCategoryItem
import jieba

class CategorySpider(Spider):
	name="category_spider"
#	item=DoubanMovieCategoryItem()
	allowed_domains=["www.movie.douban.com"]
	start_urls=[
		'http://movie.douban.com/top250?start=225&filter=&type=',
	]

	def parse(self,response):
		sel=Selector(response)
		item=DoubanMovieCategoryItem()
		category=sel.xpath("//div[@class='info']/div[@class='bd']/p/text()").extract()

		print type(category)
		x=[]
		for i in category:

			if len(i)>5 and ':' not in i:
				i=i.split('/')
				i=i[len(i)-1]
#				print i
				i=i.strip()
				i=i.replace(" ","")
				word=unicode(i)

				if word!=" " and len(word)>0:
					
					print len(word)
					print word
					
					words=jieba.cut(word,cut_all=False)
					for n in words:
						print n
						x.append(n)
		item['categories']=x		
		yield item



		"""	
				
				word=word[len(word)-1]
				word=jieba.cut(word,cut_all=False)
				for the_word in word:
					if len(the_word)>2:
						print the_word
				print "```````````````\n"
		"""

		list=[]

"""
		for i in category:
			if len(i)>5 and ':' not in i:
				i=i.split('/')
				i=i[len(i)-1]
				i=i.strip()
				i=str(i)
				i=i.split(' ')
				i=unicode(i)
				print i
				print type(i)
#				i.split(' ')
				print type(i)
				for q in i:
					print q
#				print i[-2]
				if len(i)>1:

					start=1
					end=len(i)
					print end
"""
"""					
					while(start!=(end-2)):
						the_item=unicode(i[start:start+2])


						list.append(the_item)
						start=start+2
		item['categories']=list


		yield item
"""