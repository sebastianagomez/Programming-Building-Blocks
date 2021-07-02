chMeal = float(input("The price of a child's meal: "))
adMeal = float(input("The price of a adults's meal: "))
manyChil = int(input("How many children are there? "))
manyAdul = int(input("How many adults are there? "))
drinks = int(input("How many drinks? "))
salesTax = float(input("What is the sales tax rate? "))

formuDrinks = drinks * 0.75
formuSubtotal = chMeal * manyChil + adMeal * manyAdul + formuDrinks
formuTax = formuSubtotal * (salesTax/100)
formuTotal = formuSubtotal + formuTax

print()

print(f'Subtotal: ${formuSubtotal:.2f}')
print(f'Sales Tax: ${formuTax:.2f}')
print(f'Total: ${formuTotal:.2f}')

print()

amountPay = float(input("What is your payment amount? "))

formuChange = amountPay - formuTotal

print(f'Change: ${formuChange:.2f}')

print("Thanks for your purchase!")