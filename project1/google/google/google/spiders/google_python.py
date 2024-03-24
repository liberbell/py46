import scrapy


class GooglePythonSpider(scrapy.Spider):
    name = "google_python"
    allowed_domains = ["www.google.co.jp"]
    start_urls = ["https://www.google.co.jp"]

    def parse(self, response):
        pass
