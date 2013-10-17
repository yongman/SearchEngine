#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from pyes import *
from Website.models import Results

PAGE_SIZE=10

def dosearch(string,upage):
    conn = ES('127.0.0.1:9200', timeout=3.5)#连接ES
    fq_title = FieldQuery(analyzer='ik')
    fq_title.add('title',string)
    
    fq_content = FieldQuery(analyzer='ik')
    fq_content.add('content',string)

    bq = BoolQuery(should=[fq_title,fq_content])

    h=HighLighter(['['], [']'], fragment_size=100)
    
    page = int(upage.encode('utf-8'))
    if page < 1:
        page = 1

    s=Search(bq,highlight=h,start=(page-1)*PAGE_SIZE,size=PAGE_SIZE)
    s.add_highlight("content")
    s.add_highlight('title')
    results=conn.search(s,indices='xidian_spider',doc_types='searchEngine-type')

    list=[]
    for r in results:
        if(r._meta.highlight.has_key("title")):
            r['title']=r._meta.highlight[u"title"][0]
        if(r._meta.highlight.has_key('content')):
            r['content']=r._meta.highlight[u'content'][0]

        res = Results()
        res.content = r['content']
        res.title = r['title']
        res.url = r['url']
        list.append(res)
    return list
