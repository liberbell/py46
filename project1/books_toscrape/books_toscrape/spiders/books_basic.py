import scrapy


class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com/catalogue/category/books/fantasy_19/index.html']
    start_urls = ['http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html/']

    def parse(self, response):
        pass
