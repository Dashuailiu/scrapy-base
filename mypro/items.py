# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import MapCompose
from w3lib.html import remove_tags


class MyproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def strip_res(value):
    if value:
        return value.strip()


class DmozItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_res)
    )
    link = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_res)
    )
    desc = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_res)
    )

    def is_null(self):
        if self['title'] and self['link'] and self['desc']:
            return False
        else:
            return True



