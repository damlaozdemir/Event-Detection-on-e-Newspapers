import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from newsdata.items import NewsdataItem
class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["radikal.com.tr"]
    start_urls = [
        "http://www.radikal.com.tr/turkiye/tum_haberler/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-2/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-3/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-4/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-5/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-6/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-7/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-8/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-9/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-10/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-11/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-12/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-13/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-14/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-15/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-16/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-17/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-18/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-19/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-20/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-21/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-22/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-23/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-24/",
        "http://www.radikal.com.tr/turkiye/tum_haberler-25/",

    ]

    def parse(self, response):
        for sel in response.xpath("//div[@class='news mr20']"):
            item = NewsdataItem()
            item['title'] = sel.xpath('h2/a/text()').extract()
            item['link'] = sel.xpath('h6/a/@href').extract()
            item['desc'] = sel.xpath('h6/a/text()').extract()
            item['date'] = sel.xpath("span[@class='meta']/span[@id]/text()").extract()
            yield item
        for sel in response.xpath("//div[@class='news']"):
            item = NewsdataItem()
            item['title'] = sel.xpath('h2/a/text()').extract()
            item['link'] = sel.xpath('h6/a/@href').extract()
            item['desc'] = sel.xpath('h6/a/text()').extract()
            item['date'] = sel.xpath("span[@class='meta']/span[@id]/text()").extract()
            yield item
