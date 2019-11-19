# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SendLogItem(scrapy.Item):
    mobileId = scrapy.Field()
    md5 = scrapy.Field()
    sendMobile = scrapy.Field()
    sendTime = scrapy.Field()
    content = scrapy.Field()
    createTime = scrapy.Field()
