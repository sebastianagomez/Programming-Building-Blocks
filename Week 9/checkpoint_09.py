friends = []

name = ""

while name != "end":
    name = input("What is the name of your friend? ")

    if name != "end":
        friends.append(name)

print()
print("Your friends are:")
print()

for friend in friends:
    print(friend)