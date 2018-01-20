# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhaopinItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

class CareerItem(scrapy.Item):
	career = scrapy.Field()
	company = scrapy.Field()
