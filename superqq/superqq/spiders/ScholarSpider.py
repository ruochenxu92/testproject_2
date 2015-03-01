__author__ = 'Xiaomin'
from scrapy.spider import Spider
import scrapy
import os
import datetime
from superqq.items import ScholarItem
from superqq.utils import utils
from task.models import cs499Item

tool = utils()
recent_year = 2009

def getUrls():
    path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/scholar_urls.txt')
    file = open(path, 'r')
    li_urls = file.read().split('\n')
    return ['file://' + url for url in li_urls]


class ScholarSpider(Spider):
    name = 'scholar'
    start_urls = getUrls()

    def __init__(self):
        self.count = 0



#//*[@id="gsc_a_b"]/tr/td[1]
    def parse(self, response):
        i = 1                     # //*[@id="gsc_a_b"]/tr/td[3]/span
        for sel in response.xpath('//*[@id="gsc_a_b"]/tr'):
            item = ScholarItem()
            try:
                item['pub_date'] = sel.xpath('td[3]/span/text()').extract()[0]
            except:
                continue
            year = int(item['pub_date'])

            if (year <= recent_year):
                continue
            print year
            item['name'] = tool.once_clean(response.xpath('//*[@id="gsc_prf_in"]/text()').extract()[0])
            item['institutions'] = tool.once_clean(response.xpath('//*[@id="gsc_prf_i"]/div[3]/text()').extract()[0])
            buffer = ''
            for interest in response.xpath('//*[@id="gsc_prf_i"]/div[4]'):
                buffer += interest.xpath('a/text()').extract()[0]
                buffer += ', '
            item['interest'] = tool.once_clean(buffer)
            item['paper_title'] = tool.once_clean(sel.xpath('td[1]/a/text()').extract()[0])
            try:
                item['author_url']  = tool.once_clean(self.ifNotEmptyGetIndex(response.xpath('//*[@id="gsc_prf_ivh"]/a/@href')))
            except:
                pass
            digit = sel.xpath('td[2]/a/text()')
            i += 1
            if (len(digit) <= 2):
                yield item
            else:
                seeMore = sel.xpath('td[2]/a/@href').extract()[0]
                request = scrapy.Request(seeMore, callback=self.parseCiteDetails)
                request.meta['item'] = item
                yield request


    def parseCiteDetails(self,response):
        item = response.meta['item']
        pages = response.xpath('//*[@id="gs_ccl"]/div/div[2]/h3/a/@href')
        for page in pages:
            next_page = page.extract()[0]
            item['cite'].append(scrapy.Request(url = next_page, callback=self.parse_citation))
        return item


    def parse_citation(self,response):
        entry = cs499Item()
        entry['title'] = response.xpath('//*[@id="divmain"]/div/h1/strong/text()').extract()[0]
        authors = ''
        for au in response.xpath('//*[@id="divmain"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr/td[2]'):
            authors += au.xpath('a/text()').extract()[0] +  ', '
        entry['authors'] = authors
        entry['urllink'] = response.url
        entry['pdflink'] = response.xpath('//*[@id="divmain"]/table[1]/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/a/@href').extract()[0]


        entry.save()  #if not work change to yield
        return entry


    def ifNotEmptyGetIndex(self, item, index = 0):
		if item: #check to see it's not empty
			return item[index]
		else:
			return item
