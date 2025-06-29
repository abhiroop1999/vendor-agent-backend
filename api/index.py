# /api/index.py

from fastapi import FastAPI
from ..routes import router # Note the two dots to go up one directory

app = FastAPI()

# Include your routes from the routes.py file
app.include_router(router)
