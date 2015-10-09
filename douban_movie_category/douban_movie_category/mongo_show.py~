# -*- coding: utf-8 -*-
#encoding:utf-8

import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client['douban_category']

con=db['categories']

x=con.find_one()
x['count']=x['count']+1

for item in con.find():
    print item
    print type(item)
    print item['category']
    

    
    
