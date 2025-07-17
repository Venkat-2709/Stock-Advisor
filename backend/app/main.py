import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from models.db_models import Base
from config.database import engine
from routes import session 
from .backend_logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    
app = FastAPI(
    title="AI Investment Bot",
    description="A GenAI-powered financial advisor for personalized investment strategies.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(session.router, prefix="/api")

@app.get("/")
def read_root():
    logger.info("Application Started. Root endpoint accessed.")
    return {"status": "AI Investment Bot backend is running!"}
