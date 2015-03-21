# -*- coding: utf-8 -*-

# Scrapy settings for superqq project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'superqq'
SPIDER_MODULES = ['superqq.spiders']
NEWSPIDER_MODULE = 'superqq.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'superqq (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    #'superqq.pipelines.JsonWriterPipeline': 2,
    'superqq.pipelines.SuperqqPipeline': 1,
}
import os
import sys


from os.path import expanduser
home = expanduser("~")

project = home + '/testproject'
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
DOWNLOAD_DELAY = 120
project_setting = home + '/testproject/testproject.settings'
import django
path = os.path.abspath(project_setting)
sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
django.setup()
