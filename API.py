import requests
from requests.auth import HTTPBasicAuth

org = "your-org"
project = "your-project"
pat = "your-personal-access-token"

url = f"https://dev.azure.com/{org}/{project}/_apis/build/builds?api-version=7.1-preview.7"
response = requests.get(url, auth=HTTPBasicAuth('', pat))

print(response.json())  # Print build details
