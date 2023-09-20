
def fetch_batch_data(api_url, params_list):
    """
    Fetch data in batches to minimize API requests.
    :param api_url: The API endpoint URL
    :param params_list: List of dictionaries containing query parameters for each API request
    :return: List of responses
    """
    responses = []
    for params in params_list:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            responses.append(response.json())
        else:
            print(f"Failed to retrieve data with parameters: {params}")
    return responses
