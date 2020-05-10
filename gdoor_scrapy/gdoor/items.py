# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GdoorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    job_title = scrapy.Field()
    location = scrapy.Field()
    rating = scrapy.Field()
    days_posted = scrapy.Field()
    start_salary = scrapy.Field()
    max_salary = scrapy.Field()
    job_link = scrapy.Field()

