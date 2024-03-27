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
        driver = response.meta["driver"]
        w = driver.execute_script("return document.body.scrollWidth")
        h = driver.execute_script("return document.body.scrollHeight")
