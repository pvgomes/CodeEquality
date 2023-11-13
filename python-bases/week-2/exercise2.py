def toMilesandFar(kmAmount, cAmount):
    fahrenheit = (cAmount * 1.8) +  32
    miles = kmAmount * 0.62137119
    return "I run " + str(miles) + " in " + str(fahrenheit)

km = float(input("How much you ran? "))
celsios = float(input("At what tempeture? "))
message = toMilesandFar(km, celsios)
print(message)