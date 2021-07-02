prices = 0.5

if prices >= 1.00:
    tax = 0.7
else:
    tax = 0
print (tax)



country = "CANADA"

if country.lower() == "canada":
    print("Oh look a Canadian")
else: 
    print("You are not from Canada")



price = input("How much did you pay? ")

priceNum = float(price)
if priceNum >= 1.00:
    tax = 0.07
else:
    tax = 0
print("Tax rate is: " + str(tax))



countrys = input("Enter the name of your home country: ")
if countrys.lower() == "canada":
    print("So you must like hockey!")
else:
    print("You are not from Canada")

countryss = "Canada"
province = "Ontario"

if countryss == "Canada":
    if province in("Alberta", "Nunavut", "Yukon"):
        tax = 0.05
    elif province == "Ontario":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)