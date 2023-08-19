import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["www.gardena.com"]
    start_urls = ["https://www.gardena.com/uk/products/lawn-care/"]

    def parse(self, response):
        pass
