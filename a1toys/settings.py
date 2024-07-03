# a1toys/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot settings
BOT_NAME = "a1toys"

SPIDER_MODULES = ["a1toys.spiders"]
NEWSPIDER_MODULE = "a1toys.spiders"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# MongoDB settings
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')

# Item pipelines
ITEM_PIPELINES = {
    'a1toys.pipelines.MongoDBPipeline': 300,
}

# Discord webhook URL
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

# Logging settings
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_FILE = 'scrapy.log'

# Default request headers
DEFAULT_REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
