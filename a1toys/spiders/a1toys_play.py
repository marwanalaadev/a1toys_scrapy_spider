import scrapy
from a1toys.items import A1toysPlayItem  # Adjust the import path according to your project structure

class A1toysPlaySpider(scrapy.Spider):
    name = "a1toys_play"
    allowed_domains = ["a1toys.com"]
    start_urls = ["https://a1toys.com/"]

    def parse(self, response):
        self.logger.info('Parsing started for URL: %s', response.url)
        categories_urls = response.xpath('//div[@class="magezon-builder"]/div/a/@href').getall()
        for url in categories_urls:
            yield scrapy.Request(url, callback=self.parse_products_urls)

    def parse_products_urls(self, response):
        self.logger.info('Parsing started for URL: %s', response.url)
        products = response.xpath('//li[@class="item product product-item product-item-info"]')
        for product in products:
            item = A1toysPlayItem()
            item['title'] = product.xpath('.//img/@alt').get() or 'null'
            item['price'] = product.xpath('.//span[@class="price"]/text()').get().replace('£', '') or 'null'
            item['image'] = product.xpath('.//img/@src').get() or 'null'
            item['url'] = product.xpath('.//a/@href').get() or 'null'   
            yield item
        next_page = response.xpath('//li[@class="item pages-item-next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_products_urls)
