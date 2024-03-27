import scrapy
from scrapy_selenium import SeleniumRequest

class LuxuryWatchSpider(scrapy.Spider):
    name = "luxury_watch"

    def start_requests(self):
        yield SeleniumRequest(
            url="https://antenna.jp",
            wait_time=2,
            screenshot=False,
            callback=self.parse
        )

    def parse(self, response):
        pass
