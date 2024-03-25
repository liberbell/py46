import scrapy
from scrapy_selenium import SeleniumRequest

class GooglePythonSpider(scrapy.Spider):
    name = "google_python"

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.google.co.jp',
            wait_time = 3,
            callback = self.parse
        )

    def parse(self, response):
        driver = response.meta["driver"]
        driver.save_screenshot("01_open_google.png")
