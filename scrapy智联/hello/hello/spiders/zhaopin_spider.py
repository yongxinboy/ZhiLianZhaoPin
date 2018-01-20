import scrapy
from scrapy.selector import HtmlXPathSelector
# from scrapy.http import Request
# from urllib.request import urlopen
from scrapy.http import Request
from hello.items import ZhaopinItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
ii=0

class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]   #允许访问的域
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&p=1",
        #"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=c%2B%2B&sm=0&p=1"
    ]
    rules = [
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//a[@href]')),
             callback='parse_item',
             follow=True)
    ]
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Referer": "http://www.zhaopin.com/"
    }
    def spiderCareerInfo(self,response):
        print('----------------------------')
        hxs = HtmlXPathSelector(response)
        hxsObj = hxs.select('//div[@class="inner-left fl"]')
        careerName = hxsObj[0].select('//h1/text()').extract()
        companyName = hxsObj[0].select('//h2/a/text()').extract()
        print(careerName)
        print(companyName)
    def exec(self,response):
        print('--------------执行毁掉-----------------')
        
        print('|||||||||||||||||||||||||||||')

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        hxsObj = hxs.select('//a[@style="font-weight: bold"]')
        def fun():
                print('bbb')
        for p in hxsObj:
            url = p.select("@href").extract()
            # print(p.select("text()").extract())
            # print(url[0])
            #request = Request(url[0], callback=self.spiderCareerInfo)
            #yield Request(url=url[0], headers = self.headers,callback=self.exec,dont_filter = True)
            request = Request(url, callback=self.exec)
            yield request

    #每爬完一个网页会回调parse方法
    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        print('-------处理职位-----------')
        hxs = HtmlXPathSelector(response)
        hxsObj = hxs.select('//a[@style="font-weight: bold"]')
        for p in hxsObj:
            url = p.select("@href").extract()
            
            request = Request(url[0], callback=self.spiderCareerInfo)
            yield request
        # mm = self.parse_item(response)
        # next(mm)
        # next(mm)
        # for m in mm:
        #     pass
        
        # hxsObj = hxs.select('//a[@style="font-weight: bold"]')
        # for p in hxsObj:
        #     url = p.select("@href").extract()
        #     print(p.select("text()").extract())
        #     print(url[0])
        #     request = Request(url[0], callback=self.spiderCareerInfo)
        #     yield request
        print('-------------下一页------------------')
        hxsObj = hxs.select('//a[@class="next-page"]')
        print('---------------------')
        if len(hxsObj)==1:
            urls = hxsObj[0].select("@href").extract()
            text = hxsObj[0].select("text()").extract()
            print(urls[0])
            print(text)
            request = Request(urls[0], callback=self.parse)
            yield request


        print('##################################')