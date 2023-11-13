def convertCurrency(amount):
    conversion_rate = 4.29
    return round(amount / conversion_rate, 2)

amount = int(input("How much zlots do you wanna convert?: "))
total = convertCurrency(amount)
print("You requested to convert:", amount,"zlots into EURO, the amount of EUROs are:", total)

