# -*- coding: utf-8 -*-
import scrapy
from trade.items import TradeItem

class ZhishuaSpider(scrapy.Spider):
    name = 'qoutes'
    allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/trade/lsjysj_zhishu_000002.html?year=2018&season=4']


    def start_requests(self):
        #定义第一个请求
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def get_next_url(self, old_url):
        #传入的url格式：http://quotes.money.163.com/trade/lsjysj_zhishu_000002.html?year=2018&season=1
        l = old_url.split('=')  # 用等号分割字符串
        lx=l[1].split('&')#对2018&season进行分割构造年份
        old_year=int(lx[0])
        old_season = int(l[2])

        new_season = old_season - 1
        new_year = old_year
        if new_season == 0:
            new_year=old_year-1
            new_season=old_season+3
            if new_year==2010:# 如果new_year迭代到2015了，说明已爬取到2016年的数据，爬虫可以结束了
                return

        new_url = l[0] + "=" + str(new_year)+"&season" + "=" + str(new_season)  # 构造出新的url
        #new_url = l[0] + "=" + l[1] + "=" + str(new_season)  # 构造出新的url
        return str(new_url)  # 返回新的url

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
            next_url = self.get_next_url(response.url)  # 向get_next_url方法传递原URL，response.url就是原请求的url
            if next_url != None:  # 如果返回了新的url
                yield scrapy.Request(next_url, callback=self.parse)
