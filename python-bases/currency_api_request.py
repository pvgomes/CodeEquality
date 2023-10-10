import requests
#https://app.exchangerate-api.com/dashboard
url = 'https://v6.exchangerate-api.com/v6/2b5a68ad0e2638ee61dd3060/pair/EUR/PLN'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
#print(data)
#CONVERSION RATE
print(data['conversion_rate'])