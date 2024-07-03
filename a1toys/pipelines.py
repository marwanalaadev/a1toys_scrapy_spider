# a1toys/pipelines.py

import pymongo
import requests
from datetime import datetime

class MongoDBPipeline:
    collection_name = 'products'

    def __init__(self, mongo_uri, mongo_db, discord_webhook_url):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.discord_webhook_url = discord_webhook_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
            discord_webhook_url=crawler.settings.get('DISCORD_WEBHOOK_URL')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        product = self.db[self.collection_name].find_one({'title': item['title']})

        if product:
            old_price = float(product['price'])
            new_price = float(item['price'])
            if old_price != new_price:
                drop_percentage = ((old_price - new_price) / old_price) * 100
                sale_record = {
                    'title': item['title'],
                    'old_price': old_price,
                    'new_price': new_price,
                    'drop_percentage': drop_percentage,
                    'image': item['image'],
                    'url': item['url'],
                    'date': datetime.now()
                }
                self.db['sales'].insert_one(sale_record)
                self.db[self.collection_name].update_one(
                    {'_id': product['_id']},
                    {'$set': {
                        'price': item['price'],
                        'image': item['image'],
                        'url': item['url']
                    }}
                )
                self.send_discord_notification(sale_record)
        else:
            self.db[self.collection_name].insert_one(dict(item))

        return item

    def send_discord_notification(self, sale_record):
        message = (
            f"**Price Drop Alert!**\n"
            f"**Title:** {sale_record['title']}\n"
            f"**Old Price:** £{sale_record['old_price']}\n"
            f"**New Price:** £{sale_record['new_price']}\n"
            f"**Drop Percentage:** {sale_record['drop_percentage']:.2f}%\n"
            f"**URL:** {sale_record['url']}\n"
            f"**Date:** {sale_record['date']}\n"
        )
        data = {
            "content": message
        }
        response = requests.post(self.discord_webhook_url, json=data)
        if response.status_code != 204:
            print(f"Failed to send notification to Discord. Status code: {response.status_code}")
