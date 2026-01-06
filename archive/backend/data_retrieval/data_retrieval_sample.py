
# Data Retrieval for Space Weather Web App

import requests  # Documentation: Please describe the functionality in detail.
import json  # Documentation: Please describe the functionality in detail.

# Define the API key and base URL
api_key = "YOUR_API_KEY_HERE"
base_url = "https://sws-data.sws.bom.gov.au/api/v1/"

# Function to get the most recent A index for the Australian region
def get_a_index():  # Documentation: Please describe the functionality in detail.
    endpoint = "get-a-index"
    url = f"{base_url}{endpoint}"
    payload = {"api_key": api_key}
    response = requests.post(url, json=payload)
if response.status_code == 200:  # Documentation: Please describe the functionality in detail.
        data = response.json()
return data  # Documentation: Please describe the functionality in detail.
else:  # Documentation: Please describe the functionality in detail.
return {"error": "Failed to retrieve data"}  # Documentation: Please describe the functionality in detail.

# Function to get the most recent K index from a specified location
def get_k_index(location="Australian region"):  # Documentation: Please describe the functionality in detail.
    endpoint = "get-k-index"
    url = f"{base_url}{endpoint}"
    payload = {"api_key": api_key, "location": location}
    response = requests.post(url, json=payload)
if response.status_code == 200:  # Documentation: Please describe the functionality in detail.
        data = response.json()
return data  # Documentation: Please describe the functionality in detail.
else:  # Documentation: Please describe the functionality in detail.
return {"error": "Failed to retrieve data"}  # Documentation: Please describe the functionality in detail.

# Similarly, functions for other endpoints can be created.

# Example usage:
if __name__ == "__main__":  # Documentation: Please describe the functionality in detail.
    a_index_data = get_a_index()
    print("A Index Data:", a_index_data)
    
    k_index_data = get_k_index()
    print("K Index Data:", k_index_data)

