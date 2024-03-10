import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging


class ComputerBooksSpider(CrawlSpider):
    name = 'computer_books'
    allowed_domains = ['www.kinokuniya.co.jp']
    start_urls = ['https://www.kinokuniya.co.jp/f/dsd-101001037028005-06-']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='heightLine-2']/a"),
             callback='parse_item', follow=False),
        # Rule(LinkExtractor(restrict_xpaths="(//a[contains(text(), '次へ')])[1]"),
        #      follow=True),
    )

    def parse_item(self, response):
        logging.info(response.url)
        title = response.xpath("//h3/text()").get()
        author = response.xpath("//div[3][@class='autherPublisher']/ul/li[1]/a/text()").get()
        price = response.xpath("//span[@class='redhot st']/text()").get()
        publisher = response.xpath("//a[contains(@href, 'publisher-key')]/text()").get()
        size = response.xpath("//ul[@class='dotted mt05 pt05']/li/text()").get()
        pages = response.xpath("//ul[@class='dotted mt05 pt05']/li/text()").get()
        isbn = response.xpath("//li[@itemprop='identifier']/text()").get()

        yield {
            "title": title,
            "author": author,
            "price": price,
            "publisher": publisher,
            "size": size,
            "pages": pages,
            "isbn": isbn
        }
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
