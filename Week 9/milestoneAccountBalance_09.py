bank_account = []
balances = []

name_bank = ""
current_balance = ""

print("\nEnter the names and balances of bank accounts (type: quit when done)")

while name_bank != "quit":
    name_bank = input("\nWhat is the name of this account?\n ")

    if name_bank != "quit":
        current_balance = float(input("\nWhat is the balance?\n "))
        bank_account.append(name_bank)
        balances.append(current_balance) 

print("\nAccount Information:")

for i in range (len(bank_account)):
    name_bank = bank_account[i]
    current_balance = balances[i]
    print(f"{i}. {name_bank} - ${current_balance} ")

print(f"\nTotal: ${sum(balances)}")
print(f"Average: ${sum(balances)/len(balances):.2f}")

# STRECH CHALLENGE

highest_name = ""
highest_balance = -1

for j in range(len(balances)):
    name_bank = bank_account[i]
    current_balance = balances[i]
    if highest_balance < current_balance:
        highest_balance = current_balance
        highest_name =  name_bank
        print(f"Highest balance: {highest_name} - ${highest_balance}\n")

update = ""

while update != "no":
    update = input("\nDo you want to update an account?: ")   
    if update == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? ")) 
        balances[index] = new_amount
    
    print("\nAccount Information:")

    for k in range (len(bank_account)):
        name_bank = bank_account[k]
        current_balance = balances[k]
        print(f"{k}. {name_bank} - ${current_balance} ")