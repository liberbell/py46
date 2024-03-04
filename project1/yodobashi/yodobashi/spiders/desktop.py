import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.yodobashi.com']
    start_urls = ['https://www.yodobashi.com/category/19531/11970/34646']

    def parse(self, response):
        products = response.xpath("//div[1]/a[contains(@class, 'js_productListPostTag')]")
        # products = response.css("div > a.js_productListPostTag")

        for product in products:
            # maker = product.xpath(".//div/div[contains(@class, 'brand')]/text()").get()
            # maker = product.css("div > div.brand::text")

            name = product.xpath(".//a/div/div[2]/div[1]/strong/text()").get()
            price = product.xpath(".//div/ul/li/strong[contains(@class, 'js_ppSalesPrice')]/text()").get()

            yield {
                "maker": maker,
                "name": name,
                "price": price
            }
