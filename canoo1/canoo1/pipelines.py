# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
 
import sqlite3


import sqlite3
from itemadapter import ItemAdapter

class Canoo1Pipeline:
    def __init__(self):
        self.create_connection()
        self.spider_name = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect("canoo_inc_db_hi.db")
            self.curr = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS historical_data (
                                id INTEGER PRIMARY KEY,
                                date TEXT,
                                open_price REAL,
                                high_price REAL,
                                low_price REAL,
                                close_price REAL,
                                adj_close REAL,
                                volume INTEGER
                            )""")
        self.conn.commit()

    def process_item(self, item, spider):
        if spider.name == "historicalspider":
            if self.spider_name != spider.name:
                self.create_table()
                self.spider_name = spider.name
            try:
                self.store_data(item)
            except Exception as e:
                print("Error storing item in SQLite database:", e)
        return item

    def store_data(self, item):
        self.curr.execute("""INSERT INTO historical_data (date, open_price, high_price, low_price, close_price, adj_close, volume)
                             VALUES (?, ?, ?, ?, ?, ?, ?)""",
                          (item['date'], item['open_price'], item['high_price'], item['low_price'],
                           item['close_price'], item['adj_close'], item['volume']))
        self.conn.commit()

    def close_spider(self, spider):
        if spider.name == "historicalspider":
            self.conn.close()


# class Canoo1Pipeline:
#     def __init__(self):
#         self.create_connection()

#     def create_connection(self):
#         try:
#             self.conn = sqlite3.connect("canoo_inc_db.db")
#         except sqlite3.Error as e:
#             print("Error connecting to SQLite database:", e)

#     def close_spider(self, spider):
#         self.conn.close()

#     def process_item(self, item, spider):
#         # print("table nama", str(str(spider.name) + "_table"))
#         # print(f"Item {str(str(spider.name) + "_table")  }")
#         return item
