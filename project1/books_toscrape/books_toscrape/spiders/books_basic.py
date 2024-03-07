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
            
            if url:
                yield response.follow(url=url, callback=self.parse)
                book_upc = response.xpath("//table/tbody/tr/td/text()")
                book_reviews = response.xpath("")

            yield {
                "book_title": book_title,
                "url": url,
            }

        next_page = response.xpath("//li[@class='next']/a/@href")
        if next_page:
            yield response.follow(url=next_page[0], callback=self.parse)

