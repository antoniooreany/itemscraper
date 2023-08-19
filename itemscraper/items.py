# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryPathsItem(scrapy.Item):
    category_paths = scrapy.Field()


class ProductPathsItem(scrapy.Item):
    product_paths = scrapy.Field()


class ProductItems(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
