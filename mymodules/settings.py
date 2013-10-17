#-*- coding:utf-8 -*-

# Scrapy settings for dirbot project

SPIDER_MODULES = ['mymodules.spiders']
NEWSPIDER_MODULE = 'mymodules.spiders'
DEFAULT_ITEM_CLASS = 'mymodules.items.Website'

ITEM_PIPELINES = {
        #'mymodules.pipelines.FilterWordsPipeline':543,
       'mymodules.pipelines.DuplicatesPipeline':500,
                    
}

DOWNLOAD_DELAY = 0
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

# 广度优先搜索
SCHEDULER_ORDER = 'BFO'

DEPTH_PRIORITY = 0
DEPTH_LIMIT = 2 #设置爬虫深度

SPIDER_MIDDLEWARES = {
}
