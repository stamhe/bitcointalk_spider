#!/usr/bin/python
#coding=utf-8
# @hequan


import scrapy

from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.spiders import CrawlSpider

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from bitcointalk_spider.items import BitcointalkSpiderScrapyItem

class bitcointalk_spider(CrawlSpider):
    # 爬虫的识别名称，必须是唯一的，在不同的爬虫中你必须定义不同的名字
    name = "bitcointalk_spider"    # 设置爬虫名称

    # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ["bitcointalk.org"] # 设置允许的域名

    # 爬取的url列表，爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始，其他子url将会从这些起始url中继承性生成
    start_urls = [
        'https://bitcointalk.org/index.php?board=159.0', # 山寨币创世贴首页
    ]

    city_map = {
        "1"     : "021", # 上海
        "2"     : "010", # 北京
        "4"     : "020", # 广州
        "7"     : "0755", # 深圳
    }

    shop_type_map = {
        # 幼儿教育
        'g188'   : 110000,
        # 其他亲子服务
        'g27769' : 91000,
        # 亲子旅游
        'g33808' : 80001,
        # 亲子游乐
        'g161' : 71000,
    }

    def parse(self, response):
        sel = Selector(response)
        topic_list = sel.xpath('//td[@class="windowbg"]/span')
        for bianhao,city_id in self.city_map.items():
            for cat_id,shop_type in self.shop_type_map.items():
                next_list_url = 'http://www.dianping.com/search/category/' + bianhao + '/70/' + cat_id
                yield scrapy.Request(next_list_url, callback=self.parse)

        item = BitcointalkSpiderScrapyItem()

        item['topic_url']    = topic_url

        #yield item


