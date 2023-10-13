import requests
#https://app.exchangerate-api.com/dashboard
url = 'https://v6.exchangerate-api.com/v6/2b5a68ad0e2638ee61dd3060/pair/EUR/PLN'

# Making our request
response = requests.get(url)
data = response.json()

amount = int(input("How much zlots do you wanna convert?: "))
conversion_rate = float(data['conversion_rate'])
total = round(amount / conversion_rate, 2)
print("You requested to convert:", amount,"zlots into EURO, the amount of EUROs are:", total)
