#!/usr/bin/env python
#-*- coding:utf-8-*-
import os
import sys
from pyes import *
from mymodules.items import Website
INDEX_NAME='xidian_spider'

class SearchIndex(object):

    def SearchInit(self):
        self.conn = ES('127.0.0.1:9200', timeout=3.5)#连接ES
        try:
            self.conn.delete_index(INDEX_NAME)
            #pass
        except:
            pass
        self.conn.create_index(INDEX_NAME)#新建一个索引
        
        #定义索引存储结构
        mapping = {u'content': {'boost': 1.0,
                          'index': 'analyzed',
                          'store': 'yes',
                          'type': u'string',
                          "indexAnalyzer":"ik",
                          "searchAnalyzer":"ik",
                          "term_vector" : "with_positions_offsets"},
                  u'title': {'boost': 1.0,
                             'index': 'analyzed',
                             'store': 'yes',
                             'type': u'string',
                             "indexAnalyzer":"ik",
                             "searchAnalyzer":"ik",
                             "term_vector" : "with_positions_offsets"},
                  u'url': {'boost': 1.0,
                             'index': 'analyzed',
                             'store': 'yes',
                             'type': u'string',
                             #"indexAnalyzer":"ik",
                             #"searchAnalyzer":"ik",
                             "term_vector" : "with_positions_offsets"},
        }
        

        self.conn.put_mapping("searchEngine-type", {'properties':mapping}, [INDEX_NAME])#定义type

        
    def AddIndex(self,item):

        print 'Adding Index item URL %s'% item['title'].encode('utf-8')
        self.conn.index({'title':item['title'].encode('utf-8'), \
                'url':item['url'].encode('utf-8'),\
                'content':item['content'].encode('utf-8')\
                },INDEX_NAME,'searchEngine-type')
            
    def IndexDone(self):
        self.conn.default_indices=[INDEX_NAME]#设置默认的索引
        self.conn.refresh()#刷新以获得最新插入的文档
        

