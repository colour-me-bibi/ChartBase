# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import sqlite3


class ScrapeheroPipeline(object):
    def __init__(self):
        self.connection = sqlite3.connect('../ChartBase.db')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            'INSERT INTO links VALUES (?, ?, ?)', (item['url'], item['source'], 0))
        self.connection.commit()

        logging.log(logging.INFO, f'Item stored: {item}')

        return item
