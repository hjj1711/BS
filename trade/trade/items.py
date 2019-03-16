# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TradeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义mysql存储的表名称
    table='qoutes'
    date=scrapy.Field()#日期
    OP = scrapy.Field()#开盘价
    HP = scrapy.Field()#最高价
    LP = scrapy.Field()#最低价
    CP = scrapy.Field()#收盘价
    UD= scrapy.Field()#涨跌额
    RF = scrapy.Field()#涨跌幅(%)
    turnover = scrapy.Field()#成交量(手)
    TV = scrapy.Field()#成交金额(万元)
    # AP = scrapy.Field()#振幅(%)
    # stto = scrapy.Field()#换手率(%)

