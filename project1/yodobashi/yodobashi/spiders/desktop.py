import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.yodobashi.com/category/19531']
    start_urls = ['http://www.yodobashi.com/category/19531/']

    def parse(self, response):
        pass
