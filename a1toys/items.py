import scrapy

class A1toysPlayItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
