# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import pandas as pd
from scrapy import signals
#from scrapy.contrib.exporter import CsvItemExporter
from scrapy.exporters import CsvItemExporter
import pymysql


class TradePipeline(object):
    def process_item(self, item, spider):
        # date=item['date']
        # if date:
        # #     #item['date'] = date.datetime(item['date'], format='%Y%m%d')
        # #     item['date']=time.strftime(date,"%Y-%m-%d")
        # #     item['date'] = time.strptime("%Y-%m-%d", date)
        # #     item['date'] = datetime.datetime.strptime(date, "%Y-%m-%d")
        # #     item['date'] = time.strftime("%Y-%m-%d", date)
        #     item['date']=pd.to_datetime(date, format='%Y%m%d')
        #对爬取的数据进行处理，去除“，”号
        OP=item['OP']
        if OP:
            item['OP'] = OP.replace(',','')

        HP=item['HP']
        if HP:
            item['HP'] = HP.replace(',','')

        LP=item['LP']
        if LP:
            item['LP'] = LP.replace(',','')

        CP=item['CP']
        if CP:
            item['CP'] = CP.replace(',','')
        UD=item['UD']
        RF=item['RF']

        turnover=item['turnover']
        if turnover:
            item['turnover'] = turnover.replace(',','')

        TV=item['TV']
        if TV:
            item['TV'] = TV.replace(',','')
        return item

#定义用于保存csv文件的项目管道
class TocsvPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('./csv_file/output.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if item['date']:
            self.exporter.export_item(item)
        return item

#用于定于存储mysql的项目管道
class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        print(item['date'])
        if item['date']:
            data = dict(item)
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        return item