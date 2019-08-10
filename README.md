### 爬取bitcointalk的altcoin创世贴

#### ubuntu 系统安装
```
apt-get install libxml2 libxml2-dev software-properties-common python-dev libpython-dev libxslt1-dev libffi-dev
apt install python-mysqldb
pip2.7 install cryptography
pip2.7 install simplejson
pip2.7 install redis
pip2.7 install requests
pip2.7 install scrapy
```

#### SQL建表语句
```
CREATE TABLE `bitcointalk_altcoin` (
  `topic_url` varchar(500) NOT NULL COMMENT 'topic url',
  `status` tinyint(2) NOT NULL DEFAULT '0' COMMENT '0 未处理 1 已处理',
  `created_time` int unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`topic_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='bitcointalk的山寨币创世贴';
```