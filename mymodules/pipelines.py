from scrapy import signals
from scrapy.exceptions import DropItem
import os

from pybloomfilter import BloomFilter
from mymodules.searchIndex import SearchIndex

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion', 'xidian']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.bf = BloomFilter(10000000, 0.01, 'filter.bloom')
        self.f_write = open('visitedsites','w')
        self.si = SearchIndex()
        self.si.SearchInit()

    def process_item(self, item, spider):
        print '************%d pages visited!*****************' %len(self.bf)
        if self.bf.add(item['url']):#True if item in the BF
            raise DropItem("Duplicate item found: %s" % item)
        else:
            #print '%d pages visited!'% len(self.url_seen)
            self.save_to_file(item['url'],item['title'])
            self.si.AddIndex(item)
            return item

    def save_to_file(self,url,utitle):
        self.f_write.write(url)
        self.f_write.write('\t')
        self.f_write.write(utitle.encode('utf-8'))
        self.f_write.write('\n')

    def __del__(self):
        """docstring for __del__"""
        self.f_write.close()
        self.si.IndexDone()
