import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

RSS_FEEDS = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]