import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a/@href"), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a/@href"))
    )

    def parse_item(self, response):
        books = response.xpath("//article[@class='product_pod']")
        title = books.xpath(".//h3/a/text()").get()
        price = books.xpath()
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
