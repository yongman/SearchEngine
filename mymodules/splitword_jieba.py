#!/usr/bin/env python
# -*- coding:utf-8 -*-

import jieba

text = '工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'

default_mode = jieba.cut(text)
full_mode = jieba.cut(text,cut_all=True)
search_mode = jieba.cut_for_search(text)

print "精确模式:","/".join(default_mode)
print "全模式:","/".join(full_mode)
print "搜索引擎模式:","/".join(search_mode)

