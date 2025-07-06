# /api/index.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from routes import router

app = FastAPI()

# Include your routes from the routes.py file
app.include_router(router)
