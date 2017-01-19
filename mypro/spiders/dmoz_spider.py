# -*- coding: utf-8 -*-
import scrapy
from mypro.items import DmozItem
from scrapy.contrib.loader import ItemLoader


def strip_res(str_list):
    if str_list:
        return str_list[0].strip()
    else:
        return ""


class DomzSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://www.dmoz.org/Arts/Architecture/Archives/',
        'http://www.dmoz.org/Arts/Crafts/Paper/Origami/Origamic_Architecture/'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.selector.xpath(
                "//div[normalize-space(@id)='site-list-content'][normalize-space(@class)='results browse-content']"
                "/div[normalize-space(@class)='site-item']"
                "/div[normalize-space(@class)='title-and-desc']"):
            DmozLoader = ItemLoader(item=DmozItem(), response=response)
            DmozLoader.add_value('title', sel.xpath("a/div/text()").extract())
            DmozLoader.add_value('link', sel.xpath("a/@href").extract())
            DmozLoader.add_value('desc', sel.xpath("div[normalize-space(@class)='site-descr']/text()").extract())

            item = DmozLoader.load_item()
            if item:
                yield item
            # item = DmozItem()
            # item['title'] = strip_res(sel.xpath("a/div/text()").extract())
            # item['link'] = strip_res(sel.xpath("a/@href").extract())
            # item['desc'] = strip_res(sel.xpath("div[normalize-space(@class)='site-descr']/text()").extract())
            # if not item.is_null():
            #     yield item


