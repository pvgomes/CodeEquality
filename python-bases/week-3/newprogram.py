import requests

url = 'https://v6.exchangerate-api.com/v6/2b5a68ad0e2638ee61dd3060/pair/EUR/PLN'

response = requests.get(url)
data = response.json()
conversion_rate = data['conversion_rate']

print(conversion_rate)
