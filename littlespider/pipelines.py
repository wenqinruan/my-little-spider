# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.utils.project import get_config


class MySqlPipeline(object):
    def __init__(self):
        cfg = get_config()
        self.mysql_conn = pymysql.connect(host=cfg.get('mysql', 'host'),
                                          port=int(cfg.get('mysql', 'port')),
                                          user=cfg.get('mysql', 'user'),
                                          password=cfg.get('mysql', 'password'),
                                          database=cfg.get('mysql', 'database'),
                                          charset=cfg.get('mysql', 'charset'))
        pass

    def process_item(self, item, spider):
        cur = self.mysql_conn.cursor()
        try:
            sql_str = 'INSERT INTO t_mobile_send_log (md5, mobileId, sendMobile, sendTime, content)  VALUES (%s, %s, %s, %s, %s)'
            cur.execute(sql_str, (item['md5'], item['mobileId'], item['sendMobile'], item['sendTime'], item['content']))
            self.mysql_conn.commit()
        except:
            self.mysql_conn.rollback()
            raise
        finally:
            cur.close()

        return item

    def close_spider(self):
        self.mysql_conn.close()
