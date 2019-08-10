#!/bin/bash
# @hequan
# 批量启动爬虫
workdir=/root/hequan/bitcointalk-spider/bitcointalk_spider
cd ${workdir}
/usr/bin/python /usr/local/bin/scrapy crawl bitcointalk_spider


