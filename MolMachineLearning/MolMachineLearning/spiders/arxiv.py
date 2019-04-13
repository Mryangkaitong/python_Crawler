# -*- coding: utf-8 -*-
import scrapy
import re
from MolMachineLearning.items import MolmachinelearningItem




class ArxivSpider(scrapy.Spider):
    name = "arxiv"
    allowed_domains = ["arxiv.org"]
    start_urls = ['https://arxiv.org/list/cs.LG/pastweek?show=347']
    def parse(self, response):
        MonthPapers = response.xpath("//*[@id='dlpage']/dl")
        for each_month_papers in MonthPapers:
            papersName = each_month_papers.xpath("./dd")
            papersUrl = each_month_papers.xpath("./dt")
            papers = zip(papersName,papersUrl)
            for each_paper_name, each_paper_url in papers:
                item = MolmachinelearningItem()
                item['name'] = each_paper_name.xpath("./div/div[1]/text()").extract()[1][0:-1]
                item['url'] = ['https://arxiv.org'+each_paper_url.xpath("./span/a[2]/@href").get()+'.pdf']
                yield item