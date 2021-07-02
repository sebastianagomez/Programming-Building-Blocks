# List in Python

clients = []

newClient = ""

while newClient != "quit":
    newClient = input("What is the name of your client? ")
    clients.append(newClient)

for newClient in clients:
    print(clients)

# List with numbers

tips = [12.5, 13.58 , 8.59]

runningTotal = 0

for tipAmount in tips:
    runningTotal += tipAmount

print(f"The total is: {runningTotal:.2f}")

