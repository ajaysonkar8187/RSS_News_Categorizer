from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    pub_date = Column(DateTime)
    source_url = Column(String)
    category = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_article(title, content, pub_date, source_url, category):
    session = Session()
    article = NewsArticle(title=title, content=content, pub_date=pub_date, source_url=source_url, category=category)
    session.add(article)
    session.commit()
    session.close()

def get_all_articles():
    session = Session()
    articles = session.query(NewsArticle).all()
    session.close()
    return articles