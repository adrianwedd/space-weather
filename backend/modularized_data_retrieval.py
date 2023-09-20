
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API key from environment variables
API_KEY = os.getenv('API_KEY')

# Function to fetch data from a given API endpoint
def fetch_data_from_api(api_endpoint):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(api_endpoint, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Sample usage
if __name__ == '__main__':
    api_endpoint = 'https://api.example.com/data'
    fetched_data = fetch_data_from_api(api_endpoint)
    print(fetched_data)

import logging

# Configure logging
logging.basicConfig(filename='backend_log.log', level=logging.INFO)

# Updated function to fetch data from a given API endpoint with error handling
def fetch_data_from_api_with_error_handling(api_endpoint):
    try:
        headers = {'Authorization': f'Bearer {API_KEY}'}
        response = requests.get(api_endpoint, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            logging.error(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return None

# Sample usage
if __name__ == '__main__':
    api_endpoint = 'https://api.example.com/data'
    fetched_data = fetch_data_from_api_with_error_handling(api_endpoint)
    print(fetched_data)
