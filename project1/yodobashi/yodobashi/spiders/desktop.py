import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.yodobashi.com']
    start_urls = ['https://www.yodobashi.com/category/19531/']

    def parse(self, response):
        products = response.xpath("//div/a[contains(@class, 'js_productListPostTag')]")
        # products = response.css("div > a.js_productListPostTag")

        for product in products:
            maker = product.xpath(".//div/div[contains(@class, "brand")]/text()")

        yield {
            "products": products,
        }
