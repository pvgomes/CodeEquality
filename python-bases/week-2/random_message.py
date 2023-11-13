import requests

url = "https://kanye.rest/"
response = requests.get(url)

response.json()
#print()