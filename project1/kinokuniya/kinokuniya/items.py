# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join


class BookItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(str.lstrip),
        output_processor = Join(" ")
    )
    author = scrapy.Field()
    price = scrapy.Field()
    publisher = scrapy.Field()
    size = scrapy.Field()
    # page = scrapy.Field()
    isbn = scrapy.Field()
