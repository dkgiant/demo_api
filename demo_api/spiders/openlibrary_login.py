# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest

class OpenlibraryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid = 'register',
            formdata ={
                'username': 'dhgiang85@gmail.com',
                'password': 'Df7604129',
                'redirect': '/',
                'debug_token': '',
                'login': 'Log In'
            },
            callback= self.after_login            
        )
    
    def after_login(self, response):
        print('log in')
    # def parse(self, response):
    #     yield FormRequest(
    #         response.url,
    #         # formid = 'register',
    #         formdata = {
    #             'username': 'dhgiang85@gmail.com',
    #             'password': 'Df7604129'    
    #         },
    #         callback= self.after_login            
    #     )
    
    # def after_login(self, response):
    #     print('log in')
