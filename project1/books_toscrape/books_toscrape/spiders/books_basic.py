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
            # book_title = book.xpath(".//a/@title").get()
            url = book.xpath(".//a/@href").get()
            
            if url:
                yield response.follow(url=url, callback=self.parse_item)

        next_page = response.xpath("//li[@class='next']/a/@href")
        if next_page:
            yield response.follow(url=next_page[0], callback=self.parse)
            
    def parse_item(self, response):
        book_details = response.xpath("//div[@class='col-sm-6 product_main']")
        title = book_details.xpath(".//h1/text()").get()
        price = book_details.xpath(".//p[@class='price_color']/text()[2]").get()
        stock = book_details.xpath(".//p[@class='instock availability']/text()").get()
        raiting = book_details.xpath(".//p[contains(@class, 'star-rating')]/@class").get()
        upc = response.xpath("//th[contains(text(), 'UPC')]/following-sibling::td/text()").get()
        review = response.xpath("//th[contains(text(), 'Number of reviews')]/following-sibling::td/text()").get()

        yield {
            "title": title,
            "price": price,
            "stock": stock,
            "raiting": raiting,
            "upc": upc,
            "review": review
        }

