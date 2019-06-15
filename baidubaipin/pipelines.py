# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.log import logger
import json
import redis as r
from .settings import REDIS_HOST, REDIS_PORT, MONGODB_HOST, MONGODB_PORT
from pymongo import MongoClient
from datetime import datetime


class BaidubaipinPipeline(object):
    def __init__(self):
        self.client = r.Redis(REDIS_HOST, port=REDIS_PORT)
        self.conn = MongoClient(MONGODB_HOST, MONGODB_PORT)
        #self.conn.admin.authenticate("ggqshr", "root")
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
