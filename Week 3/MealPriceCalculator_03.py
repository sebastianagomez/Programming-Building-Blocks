chMeal = float(input("The price of a child's meal: "))
adMeal = float(input("The price of a adults's meal: "))
manyChil = int(input("How many children are there? "))
manyAdul = int(input("How many adults are there? "))
salesTax = float(input("What is the sales tax rate? "))

formuSubtotal = chMeal * manyChil + adMeal * manyAdul
formuTax = formuSubtotal * (salesTax/100)
formuTotal = formuSubtotal + formuTax

print()

print(f'Subtotal: ${formuSubtotal}')
print(f'Sales Tax: ${formuTax}')
print(f'Total: ${formuTotal}')

print()

amountPay = float(input("What is your payment amount? "))

formuChange = amountPay - formuTotal

print(f'Change: ${formuChange}')