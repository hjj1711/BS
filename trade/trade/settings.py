# -*- coding: utf-8 -*-

# Scrapy settings for trade project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'trade'

SPIDER_MODULES = ['trade.spiders']
NEWSPIDER_MODULE = 'trade.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'trade (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY=0.20#设置爬取的间隔时间
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'trade.middlewares.TradeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'trade.middlewares.TradeDownloaderMiddleware': 543,
    'trade.middlewares.RandomUserAgentMiddleware': 543,
    'trade.middlewares.ProxyMiddleware': 544
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'trade.pipelines.TradePipeline': 200,
    #'trade.pipelines.TocsvPipeline': 201,
    'trade.pipelines.MysqlPipeline': 202,
    #'scrapy_redis.pipelines.RedisPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#定义连接mysql数据库的相关变量
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'scrapydb'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306
#
# #scrapy利用scrapy_redis实现分布式爬取
# SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis_bloomfilter.queue.SpiderPriorityQueue"
# #去重
# DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# BLOOMFILTER_HASH_NUMBER=6
# BLOOMFILTER_BIT=30
# REDIS_URL = 'redis://:123456@120.77.223.186:6379'
PROXY_URL = 'http://localhost:5555/random'

# #test1-setting
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# #SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.FifoQueue"
# REDIS_URL = 'redis://:123456@120.77.223.186:6379'
# #设置保存指纹，本条设置十分重要，是保证爬取数据不重复的重要条件
# SCHEDULER_PERSIST=True
# #用于清除指纹
# #SCHEDULER_FLUSH_ON_START=True

#test2-setting布隆去重相关配置
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://:123456@120.77.223.186:6379'
BLOOMFILTER_HASH_NUMBER = 6
BLOOMFILTER_BIT = 10
#设置保存指纹，本条设置十分重要，是保证爬取数据不重复的重要条件
SCHEDULER_PERSIST=True





