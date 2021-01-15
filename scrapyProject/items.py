# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    address = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    days_on_zillow = scrapy.Field()
    brokerage = scrapy.Field()
