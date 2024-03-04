from fastapi import FastAPI, UploadFile, File, HTTPException
import json
import re
import requests
from config.py import API_KEY

from fastapi import FastAPI
from routes import router

app = FastAPI()

# Include routers
app.include_router(router)