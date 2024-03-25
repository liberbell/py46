import scrapy
from scrapy_selenium import SeleniumRequest

class GooglePythonSpider(scrapy.Spider):
    name = "google_python"
    allowed_domains = ["www.google.co.jp"]
    start_urls = ["https://www.google.co.jp"]

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.google.co.jp',
            wait_time = 3,
            callback = self.parse
        )

    def parse(self, response):
        pass
