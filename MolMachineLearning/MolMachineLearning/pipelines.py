# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import re, string
from scrapy.pipelines.files import FilesPipeline
class MolmachinelearningPipeline(object):
    def process_item(self, item, spider):
        with open(r"C:\Users\asus-\Desktop\result\paper.txt",'a') as fp:
            fp.write(item['name']+'\n')
        r = re.search(r"Deep|DNN|CNN|LSTM", item['name'])
        if r:
            return item		
class DownloadPapersPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for paper_url in item['url']:
            yield scrapy.Request(paper_url,meta={'item': item['name']})
    def file_path(self, request, response=None, info=None):
        paper_name = request.meta['item']
        paper_name = re.sub("[\*:\?<>\|/\\\"]+",'',str(paper_name))
        return 'full/%s.pdf' % paper_name
