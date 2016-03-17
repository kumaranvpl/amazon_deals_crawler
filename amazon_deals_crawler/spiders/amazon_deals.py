# -*- coding: utf-8 -*-
import scrapy


class AmazonDealsSpider(scrapy.Spider):
    name = "amazon_deals"
    allowed_domains = ["amazon.in"]
    start_urls = (
        'http://www.amazon.in/gp/goldbox/',
    )

    def parse(self, response):
        pass
