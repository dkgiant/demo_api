# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest

class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']


    def parse(self, response):
        csrf_token = response.xpath(r'//input[@name="csrf_token"]/@value').get()
        
        yield FormRequest(
            response.url,
            # formxpath = r'//form',
            formdata={
                'csrf_token' : csrf_token,
                'username' : 'admin',
                'password' : 'admin',
            },
            callback = self.after_login
        )

    def after_login(self, response):
        
        if response.xpath(r'//a[@href="/logout"]/text()').get():
            print('logged in')
