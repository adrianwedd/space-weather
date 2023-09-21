
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API key from environment variables
# TODO: In this section, you need to securely manage the API key. Avoid hardcoding the API key directly into the code. Use Python's `os` library to read the key from environment variables. You can set the environment variable using `export API_KEY=your_actual_key` in a UNIX-like shell, or use similar methods for other operating systems.

# Function to fetch data from a given API endpoint
def fetch_data_from_api(api_endpoint):
# TODO: In this section, you need to securely manage the API key. Avoid hardcoding the API key directly into the code. Use Python's `os` library to read the key from environment variables. You can set the environment variable using `export API_KEY=your_actual_key` in a UNIX-like shell, or use similar methods for other operating systems.
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
# TODO: In this section, you need to securely manage the API key. Avoid hardcoding the API key directly into the code. Use Python's `os` library to read the key from environment variables. You can set the environment variable using `export API_KEY=your_actual_key` in a UNIX-like shell, or use similar methods for other operating systems.
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
