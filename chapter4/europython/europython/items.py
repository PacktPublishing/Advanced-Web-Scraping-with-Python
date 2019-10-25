# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose, MapCompose, Join

clean_text = Compose(MapCompose(lambda v: v.strip()), Join())   

def custom_field(text):
	text = clean_text(text)
	return text.strip()
	
class EuropythonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field(output_processor=custom_field)
	author = scrapy.Field(output_processor=custom_field)
	description = scrapy.Field(output_processor=custom_field)
	date = scrapy.Field(output_processor=custom_field)
	tags = scrapy.Field(output_processor=custom_field)
