#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo
#from pymongo import Connection

# mongodb へのアクセスを確立
client = pymongo.MongoClient('localhost', 27017)

# データベースを作成 (名前: it_japan)
db = client.it_japan

# コレクションを作成 (名前: project)
co = db.project

# なんか適当に保存
co.insert_one({"電話番号": 3})

# 全部とってくる
for data in co.find():
    print data