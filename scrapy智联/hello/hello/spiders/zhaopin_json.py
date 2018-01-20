import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from hello.items import CareerItem

class ZhaopinSpider(scrapy.Spider):
	name = "zhaopinjson"
	allowed_domains = ["zhaopin.com"]   #允许访问的域
	start_urls = [
	    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&p=1",
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		hxsObj = hxs.select('//a[@style="font-weight: bold"]')
		for p in hxsObj:
			url = p.select("@href").extract()
			print(url)
			request = Request(url[0], callback=self.parse_info)
			yield request
			#print(url)

	def parse_info(self,response):
		hxs = HtmlXPathSelector(response)
		hxsObj = hxs.select('//div[@class="inner-left fl"]')
		careerName = hxsObj[0].select('//h1/text()').extract()
		companyName = hxsObj[0].select('//h2/a/text()').extract()
		print(careerName)
		print(companyName)
		careerItem = CareerItem()
		careerItem['career'] = careerName
		careerItem['company'] = companyName
		return careerItem
            