# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface



import csv

class CSVPipeline(object):

    def __init__(self):
        self.csvfile = open('zillow.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.csvfile)
        self.writer.writerow(('Street','City_State_ZipCode','Price','Bedrooms','Bathrooms','Size','Lot Size','Type',
                              'Price per Sqft','Year','Neighborhood','Time on Zillow','Views','Saves'))
        self.csvfile.close()

    def process_item(self,item,spider):
        with open('zillow.csv','a+',encoding='utf-8',newline='')as f:
            writer = csv.writer(f)
            writer.writerow( (item['street'], item['city_state'],item['price'],item['bedrooms'],item['bathrooms'],
                              item['size'],item['lot_size'],item['type'],item['price_per_sqft'],item['year'],
                              item['neighborhood'],item['time_on_zillow'],item['views'],item['saves']))
        return item

