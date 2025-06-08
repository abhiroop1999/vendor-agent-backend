import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router

# Load environment variables first
load_dotenv()

app = FastAPI()
app.include_router(router)
