# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import json
import redis as r
from .settings import REDIS_HOST, REDIS_PORT, MONGODB_HOST, MONGODB_PORT,MONGODB_USER,MONGODB_PASSWORD
from pymongo import MongoClient
from datetime import datetime
from logging import getLogger
logger = getLogger()

class BaidubaipinPipeline(object):
    def __init__(self):
        self.client = r.Redis(REDIS_HOST, port=REDIS_PORT)
        self.conn = MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.conn.admin.authenticate(MONGODB_USER, MONGODB_PASSWORD)
        self.mongo = self.conn.Baidu.Baidu
        self.count = 0

    def process_item(self, item, spider):
        self.count += 1
        if self.client.sadd("id_set", item['id']) == 0:
            return item
        self.mongo.insert_one(dict(item))
        return item

    def close_spider(self, item):
        logger.info("close spider and close file")
        # self.f.flush()
        # self.f.close()
        # self.client.shutdown()
        self.conn.close()
        with open("result.log", "a") as f:
            f.writelines("{} crawl item {} \n".format(datetime.now().strftime("%Y.%m.%d"),self.count))	
            f.flush()
['import scrapy']
['from pandas import Dataframe']
['import test']
['from pandas import Dataframe']
['import scrapy']
['import test']
['from numpy import np']
['from pandas import Dataframe']
['import scrapy']
['import scrapy']
['import test']
['import scrapy']
['from pandas import Dataframe']
['from pandas import Dataframe']
['from numpy import np']
['import scrapy']
['from numpy import np']
['import scrapy']
['import test']
['from numpy import np']
['from pandas import Dataframe']
['from pandas import Dataframe']
['from numpy import np']
['from pandas import Dataframe']
['import test']
['import scrapy']
['import test']
['from pandas import Dataframe']
['import scrapy']
['import test']
['import test']
['import scrapy']
['from numpy import np']
['from numpy import np']
['import scrapy']
['from pandas import Dataframe']
['import test']
['import test']
['import scrapy']
['import scrapy']
['from numpy import np']
['import scrapy']
['from pandas import Dataframe']
['import test']
['import test']
['from numpy import np']
['import test']
['import test']
['import test']
['import scrapy']
['import test']
['import scrapy']
['from numpy import np']
['from pandas import Dataframe']
['from numpy import np']
['from numpy import np']
['import scrapy']
['from numpy import np']
['import test']
['from pandas import Dataframe']
['from pandas import Dataframe']
['import scrapy']
['from numpy import np']
['import test']
['from pandas import Dataframe']
['from numpy import np']
['import test']
['from numpy import np']
['from numpy import np']
['import scrapy']
['import scrapy']
['from numpy import np']
['import test']
['import test']
['from numpy import np']
['from numpy import np']
['from pandas import Dataframe']
['from numpy import np']
['import test']
['from numpy import np']
['import scrapy']
['from numpy import np']
['import test']
['from numpy import np']
['import test']
['import scrapy']
['from pandas import Dataframe']
['import scrapy']
['from numpy import np']
['from pandas import Dataframe']
['import test']
['from numpy import np']
['from numpy import np']
['from numpy import np']
['from numpy import np']
['import test']
['import scrapy']
['import scrapy']
['import test']
['import test']
['import test']
['from numpy import np']
['import scrapy']
['import scrapy']
