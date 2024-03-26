import scrapy


class LuxuryWatchSpider(scrapy.Spider):
    name = "luxury_watch"
    allowed_domains = ["antenna.jp"]
    start_urls = ["https://antenna.jp"]

    def parse(self, response):
        pass
