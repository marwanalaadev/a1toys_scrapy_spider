# A1Toys Scrapy Spider

This project is a Scrapy spider for scraping product data from the A1Toys website. The spider collects information such as product titles, prices, images, and URLs. The data is stored in a MongoDB database, and notifications are sent to a Discord channel when a price drop is detected.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Pipeline](#pipeline)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/marwanalaadev/a1toys_scrapy_spider.git
    cd a1toys_scrapy_spider
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project root with the following content:**

    ```env
    MONGO_URI=mongodb://localhost:27017
    MONGO_DATABASE=a1toys
    DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
    ```

## Usage

To run the spider, use the following command:

```sh
scrapy crawl a1toys_play
```
This will start the spider and begin scraping data from the A1Toys website. The scraped data will be stored in the MongoDB database specified in the .env file.

## Configuration
MongoDB
Ensure that you have MongoDB installed and running on your machine. The default configuration expects MongoDB to be accessible at mongodb://localhost:27017.

Discord Webhook
Set up a Discord webhook URL to receive notifications about price drops. Replace YOUR_DISCORD_WEBHOOK_URL in the .env file with your actual webhook URL.

Project Structure
a1toys_scrapy_spider/
│
├── a1toys/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── a1toys_play.py
│
├── scrapy.log
├── requirements.txt
└── README.md
└── .env

Pipelines
The pipeline handles storing scraped items in a MongoDB database and sending notifications to a Discord channel when a price drop is detected.

MongoDBPipeline
open_spider(self, spider): Opens a connection to MongoDB when the spider starts.
close_spider(self, spider): Closes the MongoDB connection when the spider stops.
process_item(self, item, spider): Processes each scraped item. If the product already exists in the database and the price has changed, it updates the price and records the price drop. Otherwise, it inserts the new product.
send_discord_notification(self, sale_record): Sends a notification to the specified Discord channel about the price drop.



## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or issues, please contact:

Marwan Alaa Mohamed Elsaied
Email: marwan.alaa.dev@gmail.com
