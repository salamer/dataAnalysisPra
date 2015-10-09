# -*- coding: utf-8 -*-
#encoding:utf-8

import matplotlib.pyplot as plt
from pylab import *

import pymongo  



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



	plt.bar(data,data,0.5,facecolor='#9999ff', edgecolor='white')

#	for x,y in zip(data,category):
#		plt.text(x,y,'%.2f' % x,ha='center',va='bottom')

	plt.legend(category)
	plt.ylim(-1.25,+1.25)
	plt.show()

pic_show()