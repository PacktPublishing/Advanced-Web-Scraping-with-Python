# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.loader import ItemLoader

from europython.items import EuropythonItem


class EuropythonSpider(CrawlSpider):
	def __init__(self, year='', *args, **kwargs):
		super(EuropythonSpider, self).__init__(*args, **kwargs)
		self.year = year
		self.start_urls = ['http://ep'+str(self.year)+".europython.eu/en/events/sessions"]
		print('start url: '+str(self.start_urls[0]))
	
	name = "europython_spider"
	allowed_domains = ["ep2015.europython.eu","ep2016.europython.eu", "ep2017.europython.eu","ep2018.europython.eu","ep2019.europython.eu"]
	
	# Pattern for entries that match the conference/talks and /talks format
	rules = [Rule(LxmlLinkExtractor(allow=['conference/talks']),callback='process_response'),
	Rule(LxmlLinkExtractor(allow=['talks']),callback='process_response_europython2019')]

	def process_response(self, response):
		itemLoader = ItemLoader(item=EuropythonItem(), response=response)
		itemLoader.add_xpath('title', "//div[contains(@class, 'grid-100')]//h1/text()")
		itemLoader.add_xpath('author', "//div[contains(@class, 'talk-speakers')]//a[1]/text()")
		itemLoader.add_xpath('description', "//div[contains(@class, 'cms')]//p//text()")
		itemLoader.add_xpath('date', "//section[contains(@class, 'talk when')]/strong/text()")
		itemLoader.add_xpath('tags', "//div[contains(@class, 'all-tags')]/span/text()")
		item = itemLoader.load_item()
		return item
		
	def process_response_europython2019(self, response):
		item = EuropythonItem()
		print(response)
		item['title'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/h1/text()").extract()
		item['author'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/h5/a/text()").extract()
		item['description'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/p[3]/text()").extract()
		item['date'] = "July 2019"
		item['tags'] = response.xpath("//span[contains(@class, 'badge badge-secondary')]/text()").extract()

		return item