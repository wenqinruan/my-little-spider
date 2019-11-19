# -*- coding: utf-8 -*-
import scrapy

from littlespider.items import SendLogItem
from littlespider.uti import my_md5


class Sms1Spider(scrapy.Spider):
    name = 'sms1'
    allowed_domains = ['www.pdflibr.com']

    def start_requests(self):
        urls = [
            'https://www.pdflibr.com/SMSContent/11',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        trs = response.xpath('//table/tbody/tr')
        items = []
        for tr in trs:
            item = SendLogItem()
            url = response.request.url
            item['mobileId'] = url.split('/')[4]
            item['sendMobile'] = tr.css('td::text')[1].get()
            item['content'] = tr.css('td::text')[2].get()
            item['sendTime'] = tr.css('td time::text').get()
            item['md5'] = my_md5(item['mobileId'] % item['content'] % item['sendTime'])
            items.append(item)

        return items
