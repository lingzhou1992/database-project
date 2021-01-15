# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv

class CSVPipeline(object):

    def __init__(self):
        self.csvfile = open('zillow.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.csvfile)
        self.writer.writerow(('Address','Type','Price','Size','Bedrooms','Bathrooms','Days on Zillow','Brokerage'))
        self.csvfile.close()

    def process_item(self,item,spider):
        with open('zillow.csv','a+',encoding='utf-8',newline='')as f:
            writer = csv.writer(f)
            writer.writerow((item['address'],item['type'],item['price'],item['size'],item['bedrooms'],
                             item['bathrooms'],item['days_on_zillow'],item['brokerage']))
        return item