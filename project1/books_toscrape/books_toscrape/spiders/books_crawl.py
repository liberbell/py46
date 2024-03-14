import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a/@href"))
    )

    def parse_item(self, response):
        books = response.xpath("//article[@class='product_pod']")
        title = books.xpath(".//h3/a/text()").getall()
        price = books.xpath(".//div[@class='product_price']/p/text()").get()
        stock = books.xpath(".//div/p[@class='instock availability']/text()").get()
        rating = books.xpath("")
        
        yield {
            "title": title,
            "price": price,
            "stock": stock
        }
