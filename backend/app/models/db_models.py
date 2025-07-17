from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from config.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    session_id = Column(String, nullable=True) 

class RiskProfile(Base):
    __tablename__ = "risk_profile"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    risk_level = Column(String)
    investment_goal = Column(String)
    preferred_sectors = Column(Text)

class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    asset = Column(String)
    quantity = Column(Float)
    avg_price = Column(Float)

class MarketData(Base):
    __tablename__ = "market_data"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    date = Column(DateTime)
    price = Column(Float)
    volume = Column(Float)

class NewsArticle(Base):
    __tablename__ = "news_articles"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    source = Column(String)
    published_at = Column(DateTime)

class SentimentMetric(Base):
    __tablename__ = "sentiment_metrics"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    sentiment_score = Column(Float)
    related_to = Column(String)
    timestamp = Column(DateTime)

class MacroIndicator(Base):
    __tablename__ = "macro_indicators"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)
    country = Column(String)
    date = Column(DateTime)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    message = Column(Text)
    triggered_on = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
