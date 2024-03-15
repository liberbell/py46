# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    publisher = scrapy.Field()
    size = scrapy.Field()
    # page = scrapy.Field()
    isbn = scrapy.Field()
