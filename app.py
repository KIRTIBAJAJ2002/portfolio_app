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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/project_images")
def get_project_images(project_name: str):
    image_url = find_image_url(project_name)
    if image_url:
        return {"image_url": image_url}
    else:
        return {"message": "No image found for the given project name."}