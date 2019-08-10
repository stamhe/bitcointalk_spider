# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
import time

class BitcointalkSpiderScrapyPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456', charset='utf8')
        self.conn.autocommit(True)
        self.conn.select_db('db_bitcointalk')
    def process_item(self, item, spider):
        if not item:
            return item

        cursor=self.conn.cursor()
        data = []
        #date_time = time.strftime("%Y-%m-%d", time.localtime())
        timestamp = int(time.time())
        if spider.name == 'bitcointalk_spider':
            
            cursor.execute("select * from bitcointalk_altcoin where topic_url = " + item['topic_url'])
            result = cursor.fetchone()
            if result != None:
                cursor.close();
                return item;
            
            data.append(item['topic_url'])
            data.append(0)
            data.append(timestamp)
            cursor.execute('replace into bitcointalk_altcoin (topic_url, status, created_time) values (%s, %s, %s)', data)
        
        cursor.close()
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.conn.close()
