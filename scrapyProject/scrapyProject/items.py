# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Real Estate inevestment
# traffic congestion, school ratings, life quality, and crime rates
# occupancy rates, average rental income, and even the ROI of the area

import scrapy


class ScrapyprojectItem(scrapy.Item):
    price = scrapy.Field()
    type = scrapy.Field()
    year = scrapy.Field()
    lot_size = scrapy.Field()
    price_per_sqft = scrapy.Field()
    street = scrapy.Field()
    city_state = scrapy.Field()
    size = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    time_on_zillow = scrapy.Field()
    views = scrapy.Field()
    saves = scrapy.Field()
    neighborhood = scrapy.Field()

