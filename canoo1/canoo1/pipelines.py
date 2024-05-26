# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

import scrapy

class Canoo1Pipeline:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect("canoo_inc_db.db")
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # print("table nama", str(str(spider.name) + "_table"))
        # print(f"Item {str(str(spider.name) + "_table")  }")
        return item
