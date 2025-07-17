import yfinance as yf
import logging
from sqlalchemy.orm import Session
from datetime import datetime
from models.db_models import MarketData

logger = logging.getLogger(__name__)

def fetch_and_store_stock_data(symbol: str, db: Session, period: str = "5d", interval: str = "1d"):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period, interval=interval)
        
        logger.info(f"Fetching data for {symbol} - {len(hist)} records found")

        for date, row in hist.iterrows():
            db.add(MarketData(
                symbol=symbol,
                date=date.to_pydatetime() if isinstance(date, datetime) else datetime.strptime(str(date), "%Y-%m-%d"),
                price=row["Close"],
                volume=row["Volume"]
            ))

        db.commit()
        logger.info(f"Saved {len(hist)} records for {symbol}")
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to fetch/store {symbol}: {e}")