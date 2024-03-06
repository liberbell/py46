import scrapy


class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        books = response.xpath("//li/article[@class='product_pod']")
        # books = response.xpath("//h3")

        # yield {
        #     "books": books
        # }

        for book in books:
            book_title = book.xpath(".//a/@title").get()
            url = book.xpath(".//a/@href").get()

            yield {
                "book_title": book_title,
                "url": url,
            }
