# /api/index.py

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routes
try:
    from routes import router
    app.include_router(router)
    routes_status = "loaded"
except Exception as e:
    routes_status = f"failed: {str(e)}"

@app.get("/")
def root():
    return {"message": "API is running", "routes": routes_status}

@app.get("/test")
def test():
    return {"test": "working"}
