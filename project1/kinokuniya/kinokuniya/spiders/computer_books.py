import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging
from kinokuniya.items import BookItem
from scrapy.loder import Itemloder


class ComputerBooksSpider(CrawlSpider):
    name = 'computer_books'
    allowed_domains = ['www.kinokuniya.co.jp']
    start_urls = ['https://www.kinokuniya.co.jp/f/dsd-101001037028005-06-']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='heightLine-2']/a"),
             callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="(//a[contains(text(), '次へ')])[1]"),
             follow=True),
    )

    def get_title(self, title):
        if title:
            return '  '.join(title).lstrip()
        return title
    
    def get_price(self, price):
        if price:
            return int(price.replace('¥', '').replace(',', ''))
        return 0
    
    def get_size(self, size):
        if size:
            logging.info(size)
            size = size.replace("\n")[2]
            logging.info(size)
            return size
        return size
    
    def get_page(self, page):
        if page:
            return page.split("/")[0].replace("\n", "").replace("p", "")
        return page
    
    def get_isbn(self, isbn):
        if isbn:
            return isbn.replace("商品コード ", "")
        return isbn

    def parse_item(self, response):
        logging.info(response.url)
        title = response.xpath("//h3[@itemprop='name']/text()").getall()
        author = response.xpath("//div[@class='infobox ml10 mt10']/ul/li[1]/a/text()").get()
        price = response.xpath("//span[@itemprop='price']/text()").get()
        publisher = response.xpath("//a[contains(@href, 'publisher-key')]/text()").get()
        size = response.xpath("normalize-space(//ul[@class='dotted mt05 pt05']/li[1]/text())").get()
        pages = response.xpath("normalize-space(//ul[@class='dotted mt05 pt05']/li/text())").getall()
        isbn = response.xpath("//li[@itemprop='identifier']/text()").get()

        loader = Itemloder(item=BookItem(), response=response)
        loader.add_xpath("title", "//h3[@itemprop='name']/text()")
        loader.add_xpath("author", "//div[@class='infobox ml10 mt10']/ul/li[1]/a/text()")
        loader.add_xpath("price", "//span[@itemprop='price']/text()")
        loader.add_xpath("publisher", "//a[contains(@href, 'publisher-key')]/text()")


        yield {
            "title": self.get_title(title),
            "author": author,
            "price": self.get_price(price),
            "publisher": publisher,
            "size": self.get_size(size),
            "pages": pages,
            "isbn": self.get_isbn(isbn)
        }
