# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymongo

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
        self.client = pymongo.MongoClient("mongodb+srv://mongo_user:Wx5HcS6Edw1VjDq5@cluster0.4zuzwrb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["BOOKDB"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))