import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables first
logger.info("Loading environment variables...")
load_dotenv()

# Check for API key after loading
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY not found!")
else:
    logger.info("OPENAI_API_KEY loaded successfully.")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup complete.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown.")

app.include_router(router)

logger.info("FastAPI app initialized.")
