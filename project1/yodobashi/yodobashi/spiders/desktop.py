import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.yodobashi.com']
    start_urls = ['https://www.yodobashi.com/category/19531/11970/34646']

    def parse(self, response):
        products = response.xpath("//div[3]/div[contains(@class, 'productListTile')]")
        # products = response.css("div > a.js_productListPostTag")
        # brands = response.xpath("//a/div[2][contains(@class, 'pName')]/p[1]/text()").getall()
        # names = response.xpath("//a/div[2][contains(@class, 'pName')]/p[2]/text()").getall()

        # yield {
        #     "products": products,
        #     "brands": brands,
        #     "names": names
        # }


        for product in products:
            brand = product.xpath(".//a/div[2][contains(@class, 'pName')]/p[1]/text()").get()
            # maker = product.css("div > div.brand::text")

            name = product.xpath(".//div[contains(@class, 'pName')]/p[2]/text()").get()
            price = product.xpath(".//ul/li[2]/span[contains(@class, 'productPrice')]/text()").get()

            yield {
                "brand": brand,
                "name": name,
                "price": price
            }

        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callable=self.parse)
