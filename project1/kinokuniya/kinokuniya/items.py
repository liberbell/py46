# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import functools
# import hashlib
# from contextlib import suppress
# from io import BytesIO

# from itemadapter import ItemAdapter
# from PIL import Image

# from scrapy.exceptions import DropItem
# from scrapy.http import Request
# from scrapy.pipelines.files import FileException, FilePipeline
# from scrapy.settings import Settings
# from scrapy.utils.misc import md5sum
# from scrapy.utils.python import to_bytes

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

# class NoimageDrop(DropItem):
#     pass

# class ImageException(FileException):
#     pass

# class ImagePipeline(FilePipeline):
    

    # MEDIA_NAME = "image"
    # MIN_WIDTH = 0
    # MIN_HEIGHT = 0
    # EXPIRES = 90
    # THUMBS = {}
    # DEFAULT_IMAGES_URL_FIELD = "image_urls"
    # DEFAULT_IMAGES_RESULT_FIELD = "images"

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

def get_size(element):
    if element:
        return element.split("／")[0].replace("サイズ ", "").replace("判", "")
    return element

def get_page(element):
    if element:
        return element.split("／")[1].replace("ページ数 ", "").replace("p", "")
    return element

def strip_item(element):
    if element:
        return element.replace("商品コード ", "")
    return element

class BookItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(str.lstrip),
        output_processor = Join(" ")
    )
    author = scrapy.Field(
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(strip_yen, strip_comma, convert_int),
        output_processor = TakeFirst()
    )
    publisher = scrapy.Field(
        output_processor = TakeFirst()
    )
    size = scrapy.Field(
        input_processor = MapCompose(get_size),
        output_processor = TakeFirst()
    )
    # page = scrapy.Field(
    #     input_processor = MapCompose(get_page, convert_int),
    #     output_processor = TakeFirst()
    # )
    isbn = scrapy.Field(
        input_processor = MapCompose(strip_item, convert_int),
        output_processor = TakeFirst()
    )

    image_urls = scrapy.Field()
