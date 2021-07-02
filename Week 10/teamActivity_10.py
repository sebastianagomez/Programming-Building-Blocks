nameBanks = []
bankBalances = []

bankItem = ""
balanceItem = ""


print("\nEnter the names and balances of bank accounts (type: quit when done)\n")

while bankItem != "quit":
  
    bankItem = input("What is the name of this account? ")    

    if bankItem != "quit":
        balanceItem = float(input("What is the balance? "))
        nameBanks.append(bankItem)
        bankBalances.append(balanceItem)

print()
print("Account Information:")
print()

for i in range (len(nameBanks)):
    name_bank = nameBanks[i]
    current_balance = bankBalances[i]
    print(f"{i}. {name_bank} - ${current_balance}")

print()

print(f"Total: ${sum(bankBalances)}")
print(f"Average: ${sum(bankBalances)/len(bankBalances)}")

questionUpdate = input("\nDo you want to update an account? ")

if questionUpdate == "yes":
    updateAccount = int(input("What account index do you want to update? "))
    bankBalances.pop(updateAccount)
    newAmount = float(input("What is the new amount? "))
    bankBalances.append(newAmount)

else:
    print("Thanks.")

print()

print(f"Total: ${sum(bankBalances)}")
print(f"Average: ${sum(bankBalances)/len(bankBalances)}")


