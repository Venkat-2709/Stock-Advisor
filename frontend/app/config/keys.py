import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file if they exist
load_dotenv()

logger = logging.getLogger(__name__)

class Settings:
    def __init__(self):
        # Set up the Key Vault client
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.FASTAPI_URL = os.getenv("FASTAPI_URL")
        self.NEWS_URL = os.getenv("NEWS_URL")
        self.YAHOO_FINANCE_URL = os.getenv("YAHOO_FINANCE_URL")
        self.REDIS_HOST = os.getenv("REDIS_HOST")
        self.REDIS_PORT = os.getenv("REDIS_PORT")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        logger.info("Settings initialized with environment variables.")
        
# Instantiate the settings
settings = Settings()