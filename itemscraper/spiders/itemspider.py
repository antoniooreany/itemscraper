import logging

import scrapy

from ..items import ProductItems, ProductPathsItem


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["www.gardena.com"]
    start_urls = ["https://www.gardena.com/uk/products/lawn-care/"]

    def parse(self, response):
        category_paths = response.xpath(
            "//div[@class='col-xs-12']/a[@class='btn btn-primary btn-icon more-btn']").xpath('@href').extract()
        for category_path in category_paths:
            category_url = "https://www.gardena.com" + category_path
            # self.log(category_url, logging.WARN)
            yield response.follow(category_url, callback=self.parse_category_page)

    def parse_category_page(self, response):
        item = ProductPathsItem()
        product_paths = response.xpath(
            "//div[@class='row flex-container article-list-container']/div[@class='c-gar-article-list-item ']/div[@class='article-wrapper']/div[@class='bottom-part']/div[@class='see-more']/a[@class='btn btn-primary btn-block btn-icon']").xpath(
            '@href').extract()
        for product_path in product_paths:
            product_url = "https://www.gardena.com" + product_path
            self.log(product_url, logging.WARN)
            item['product_paths'] = product_paths
            yield response.follow(product_url, callback=self.parse_item_page)

    def parse_item_page(self, response):
        items = ProductItems()

        # Category
        category = response.css(
            "#MainContentPlaceHolder_MainContentPlaceHolder_ctl00_articleIntro_Breadcrumbs_breadcrumbSection li:nth-child(4) a::text")[
            0].extract()
        items['category'] = category.strip()

        # Title
        title = response.css(
            "#MainContentPlaceHolder_MainContentPlaceHolder_ctl00_articleIntro_Breadcrumbs_breadcrumbSection span::text")[
            0].extract()
        items['title'] = title.strip()

        # Description
        description = response.css("div.description-text::text")[0].extract()
        items['description'] = description.strip()

        yield items
