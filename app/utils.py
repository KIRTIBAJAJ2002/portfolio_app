import requests
import json
from config import API_KEY, SECRET_KEY

def find_image_url(project_title):
    access_key = API_KEY
    search_query = project_title.replace(' ', '+')

    # Make a request to the Unsplash API
    search_url = f'https://api.unsplash.com/search/photos?query={search_query}&per_page=1'
    headers = {
        'Authorization': f'Client-ID {access_key}'
    }
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()

    # Parse the JSON response
    data = json.loads(response.text)
    if 'results' in data and len(data['results']) > 0:
        image_url = data['results'][0]['urls']['regular']
        return image_url

    return None

def extract_project_names(resume_text):   # new code
    # Use regular expression to find project names in the resume
    project_names = re.findall(r'Project Name: (.+)', resume_text)
    return project_names
