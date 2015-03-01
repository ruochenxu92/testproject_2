__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import os
from superqq.items import FacultyItem
import datetime
import json
from superqq.utils import utils

tool = utils()
def getUrls():
    return ['http://illinois.edu/ds/detail?departmentId=illinois.eduKP434']

class CS499Spider(Spider):
    name = 'faculty'
    start_urls = getUrls()

    def __init__(self):
        self.count = 0

    def parse(self, response):
        for sel in response.xpath('//*[@id="thing_1"]/tbody/tr'):
            item = FacultyItem()
            name = sel.xpath('td[1]/a')
            print name
            # li = name.split(',')
            # item['name'] = ' '.join([li[1],li[0]])
            item['email'] = sel.xpath('td[3]/a').extract()[0]
            yield item

    def parseMovieDetails(self,response):
        item = FacultyItem()
        name = response.xpath('//*[@id="mobile-content"]/h4/text()').extract()[0]
        li = name.split()
        item['name'] = ' '.join([li[0], li[-1]])
        item['email'] = response.xpath('//*[@id="mobile-content"]/div[3]/div[3]/span/a/text()').extract()[0]
        try:
            item['faculty_url'] = response.xpath('//*[@id="ws-pos-1"]/p[1]/a').extract()[0]
        except:
            pass
        return item