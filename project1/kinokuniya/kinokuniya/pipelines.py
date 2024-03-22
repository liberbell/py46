# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymongo
import sqlite3
from scrapy.pipelines.images import ImagesPipeline

class customImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        name = item.get("isbn") + ".jpg"
        filename = r"computer_books\\" + name
        print(filename)
        return filename

# class KinokuniyaPipeline:
#     def process_item(self, item, spider):
#         return item

class CheckItemPipeline:
    def process_item(self, item, spider):
        if not item.get("isbn"):
            raise DropItem("Missing ISBN")
        return item
    
class MongoPipeline:
    collection_name = "computer_books"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://mongo_user:@cluster0.4zuzwrb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["BOOKDB"]

    def close_spider(self, item, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("BOOKDB.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute("""
    CREATE TABLE computer_books(
                        title TEXT,
                        author TEXT,
                        price INTEGER,
                        publisher TEXT,
                        size TEXT,
                        isbn INTEGER primary key
    )
                        """)
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def process_item(self, item, spider):
        self.c.execute("""
INSERT INTO computer_books (title, author, price, publisher, size, isbn)
values(?, ?, ?, ?, ?, ?)
        """, (
            item.get("title"),
            item.get("author"),
            item.get("price"),
            item.get("publisher"),
            item.get("size"),
            item.get("isbn")
        ))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()