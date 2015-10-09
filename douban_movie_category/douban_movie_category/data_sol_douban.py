# -*- coding: utf-8 -*-
#encoding:utf-8

import matplotlib.pyplot as plt
from pylab import *

import pymongo  
from matplotlib.font_manager import FontProperties
import subprocess
import numpy as np


font=FontProperties(fname=r'/usr/share/fonts/truetype/字体管家扁黑体.ttf',size=14)


def pic_show():
	client=pymongo.MongoClient("localhost",27017)

	db=client['douban_category']

	con=db['categories']

	data=[]
	category=[]

	for item in con.find():
		data.append(item['count'])
		category.append(item['category'])

	print data
	for n in  category:
		print n



#	plt.bar(data,data,0.5,facecolor='#9999ff', edgecolor='white')

#	for x,y in zip(data,category):
#		plt.text(x,y,'%.2f' % x,ha='center',va='bottom')

#	plt.legend(category)
#	plt.ylim(-1.25,+1.25)
	
	y_pos=range(len(category))
	
	colors = np.random.rand(len(category))
	
	plt.barh(y_pos,data,align='center',alpha=0.4)
	plt.yticks(y_pos,category,fontproperties=font)
	for data,y_pos in zip(data,y_pos):
		plt.text(data,y_pos,data,horizontalalignment='center',verticalalignment='center', weight='bold')
	plt.ylim(+28.0,-1.0)
	plt,title(u"豆瓣电影top250部分类统计",fontproperties=font)
	plt.ylabel(u"电影分类",fontproperties=font)
#	plt.show()
	plt.subplots_adjust(bottom = 0.15)
	plt.xlabel(u"分类出现次数（一部影片分类可以多个）",fontproperties=font)
	plt.savefig("douban_category_new.png")	
	
#	area=[data*0.05 for data in data]

"""
	plt.scatter(data,y_pos,alpha=0.8,c=colors,s=(data*60))
	
	
	plt,title(u"豆瓣电影top250部分类统计",fontproperties=font)
#	plt.ylabel(u"电影分类",fontproperties=font)
#	plt.show()
#	plt.subplots_adjust(bottom = 0.15)
	plt.xlabel(u"分类出现次数（一部影片分类可以多个）",fontproperties=font)
	
	plt.savefig("scatter.png")
	


	plt.barh(y_pos,data,align='center',alpha=0.4)
	plt.yticks(y_pos,category,fontproperties=font)
	for data,y_pos in zip(data,y_pos):
		plt.text(data,y_pos,data,horizontalalignment='center',verticalalignment='center', weight='bold')
	plt.ylim(+28.0,-1.0)
	plt,title(u"豆瓣电影top250部分类统计",fontproperties=font)
	plt.ylabel(u"电影分类",fontproperties=font)
#	plt.show()
	plt.subplots_adjust(bottom = 0.15)
	plt.xlabel(u"分类出现次数（一部影片分类可以多个）",fontproperties=font)
	plt.savefig("douban_category_new.png")	

"""
	
pic_show()
