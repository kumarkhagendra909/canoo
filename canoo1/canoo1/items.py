# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class Canoo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
class MainSpiderItem(scrapy.Item):
    label = scrapy.Field()
    value = scrapy.Field()

class ProfileSpiderItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    pay = scrapy.Field()
    exercised = scrapy.Field()
    year_born = scrapy.Field()

class HistoricalSpiderItem(scrapy.Item):
    date = scrapy.Field()
    open_price = scrapy.Field()
    high_price = scrapy.Field()
    low_price = scrapy.Field()
    close_price = scrapy.Field()
    adj_close = scrapy.Field()
    volume = scrapy.Field()