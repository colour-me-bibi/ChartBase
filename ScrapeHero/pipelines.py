import pymongo
from scrapy.exceptions import DropItem
import logging

class ScrapeheroPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient('localhost', 27017)
        db = connection['ScrapeHero']
        self.collection = db['songs']
    
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(item))
            logging.log(logging.DEBUG, 'Song added to the MongoDB database!')
        return item
