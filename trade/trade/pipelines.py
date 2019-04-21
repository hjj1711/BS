# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
from scrapy import signals
from scrapy.exporters import CsvItemExporter

class TradePipeline(object):
    def process_item(self, item, spider):
        return item


class TocsvPipeline(object):

    # def __init__(self):
    #     # csv文件的位置,无需事先创建
    #     store_file = os.path.dirname(__file__) + '/spiders/qtw.csv'
    #     # 打开(创建)文件
    #     self.file = open(store_file, 'wb')
    #     # csv写法
    #     self.writer = csv.writer(self.file)
    #
    # def process_item(self, item, spider):
    #     # 判断字段值不为空再写入文件
    #     if item['date']:
    #         self.writer.writerow()
    #     return item
    #
    # def close_spider(self, spider):
    #     # 关闭爬虫时顺便将文件保存退出
    #     self.file.close()

    def __init__(self):
        self.files = {}
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        #该打开文件的写法存在无法写入内容的问题
        #self.file = open('./csv_file/output.csv', 'w+b')
        self.file = open('%s.csv' % spider.name, 'w+b')
        #self.files[spider] = file
        self.exporter=CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if item['date']:
            self.exporter.export_item(item)
        return item


    # @classmethod
    # def from_crawler(cls, crawler):
    #     pipeline = cls()
    #     crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    #     crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    #     return pipeline
    #
    # def spider_opened(self, spider):
    #     file = open('%s_items.csv' % spider.name, 'w+b')
    #     self.files[spider] = file
    #     self.exporter = CsvItemExporter(file)
    #     self.exporter.start_exporting()
    #
    # def spider_closed(self, spider):
    #     self.exporter.finish_exporting()
    #     file = self.files.pop(spider)
    #     file.close()
    #
    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
