from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import PyPDF2
import json
import os
from app import app
from app.utils import allowed_file, extract_resume_data
from app.llmapi import formatdata
from fastapi import APIRouter
from getimages import upload_resume

router = APIRouter()

@router.post("/upload/")
async def upload_resume():
    # Implement the logic to handle resume uploads
    # This route will trigger the processing of the uploaded resume,
    # which includes formatting the data and creating a GitHub repository
    # You can call the functions from getimages.py and llmapi.py here
    pass
import json

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


with open("app/configtemplate.json","r") as configfile:
    config_data=json.load(configfile)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    resume = request.files['resume']
    
    if resume.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if resume and allowed_file(resume.filename):
        
        filename = secure_filename(resume.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(temp_path)
        
        extracted_data = extract_resume_data(temp_path)
        required_link=formatdata(extracted_data)
        print(required_link)
        os.remove(temp_path)
        
        return jsonify(required_link), 200
    
    return jsonify({'error': 'Invalid file type'}), 400
