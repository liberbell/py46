# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

def strip_yen(element):
    if element:
        return element.replace("¥", "")
    return element

def strip_comma(element):
    if element:
        return element.replace(",", "")
    return element

def convert_int(element):
    if element:
        return int(element)
    return 0

class BookItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(str.lstrip),
        output_processor = Join(" ")
    )
    author = scrapy.Field(
        output_processor = TakeFirst()
    )
    price = scrapy.Field(

    )
    publisher = scrapy.Field()
    size = scrapy.Field()
    # page = scrapy.Field()
    isbn = scrapy.Field()
