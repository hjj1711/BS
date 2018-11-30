# -*- coding: utf-8 -*-
import scrapy
from trade.items import TradeItem

class ZhishuaSpider(scrapy.Spider):
    name = 'qoutes'
    allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/trade/lsjysj_zhishu_000002.html?year=2018&season=1']

    def parse(self, response):
        item_nodes = response.css('.table_bg001.border_box.limit_sale tr')

        for item_node in item_nodes:
            item = TradeItem()
            item['date'] = item_node.css('td:nth-child(1)::text').extract_first()
            item['OP'] = item_node.css('td:nth-child(2)::text').extract_first()
            item['HP'] = item_node.css('td:nth-child(3)::text').extract_first()
            item['LP'] = item_node.css('td:nth-child(4)::text').extract_first()
            item['CP'] = item_node.css('td:nth-child(5)::text').extract_first()
            item['UD'] = item_node.css('td:nth-child(6)::text').extract_first()
            item['RF'] = item_node.css('td:nth-child(7)::text').extract_first()
            item['turnover'] = item_node.css('td:nth-child(8)::text').extract_first()
            item['TV'] = item_node.css('td:nth-child(9)::text').extract_first()
            # item['AP'] = item_node.css('td:nth-child(10)::text').extract_first()
            # item['stto'] = item_node.css('td:nth-child(11)::text').extract_first()
            yield item
