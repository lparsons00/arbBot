# run "scrapy crawl scrapeSportsbet.py -O test.json"

import scrapy

class SportsBetSpider(scrapy.Spider):
	name = "odds"

	def start_requests(self):
		urls = [
			"https://www.sportsbet.com.au/betting/soccer/united-kingdom/english-premier-league"
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
			
	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.css('li.cardOuterItem_fn8ai8t'))
		for post in response.css('li.cardOuterItem_fn8ai8t'):
			yield{
				'Home' : post.xpath('.//span[@class="size12_fq5j3k2 normal_fgzdi7m caption_f4zed5e"]/text()')[0].get(),
				'Odds 1' : post.xpath('.//span[@class="size14_f7opyze medium_f1wf24vo priceTextSize_frw9zm9"]/text()')[0].get(),
				'Draw' : post.xpath('.//span[@class="size12_fq5j3k2 normal_fgzdi7m caption_f4zed5e"]/text()')[1].get(),
				'Odds 2' : post.xpath('.//span[@class="size14_f7opyze medium_f1wf24vo priceTextSize_frw9zm9"]/text()')[1].get(),
				'Away' : post.xpath('.//span[@class="size12_fq5j3k2 normal_fgzdi7m caption_f4zed5e"]/text()')[2].get(),
				'Odds 3' : post.xpath('.//span[@class="size14_f7opyze medium_f1wf24vo priceTextSize_frw9zm9"]/text()')[2].get()
			}