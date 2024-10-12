import feedparser
from datetime import datetime
from classifier import categorize_text
import pandas as pd

RSS_FEEDS = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://qz.com/feed',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.reuters.com/reuters/businessNews',
    'http://feeds.feedburner.com/NewshourWorld',
    'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
]

def parse_feeds():
    articles = []
    
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries:
                title = entry.get('title', '')
                content = entry.get('summary', '')
                
                article = {
                    'title': title,
                    'content': content,
                    'source_url': entry.get('link', ''),
                    'publication_date': entry.get('published', ''),
                    'source': feed_url,
                    'category': categorize_text(title + " " + content)
                }
                articles.append(article)
                
        except Exception as e:
            print(f"Error parsing feed {feed_url}: {str(e)}")
    
    return pd.DataFrame(articles)