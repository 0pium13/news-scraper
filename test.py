import requests

API_KEY = "93d3d9634aac4a5c82ac95240946c384"
TEST_URL = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=1&apiKey={API_KEY}"

response = requests.get(TEST_URL)
print(response.json())  # Print the raw response