import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Define the URL
url = "https://api.bnm.gov.my/public/fx-turn-over"

# Define the header parameters
headers = {
    "Accept": "application/vnd.BNM.API.v1+json"
}

# Perform a GET request
response = session.get(url, headers=headers)
 
import requests
import json


# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)

    # Print or manipulate the data as needed
    print(data)
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
