itemList = []

item = ""

print("\nPlease enter the items of the shopping list (type: quit to finish):\n")

while item != "quit":
  
    item = input("Item: ")

    if item != "quit":
        itemList.append(item)

print()
print("The shopping list is:")
print()

for items in itemList:
    print(items)

print()
print("The shopping list with indexes is:")
print()

for i in range(len(itemList)):
    list = itemList[i]
    print(f"{i}. {list}")

print()

changeItem = int(input("What item would you like to change: "))
newItem = input("What is the new item:")

itemList.pop(changeItem)
itemList.append(newItem)

print()
print("The shopping list with indexes is:")
print()

for i in range(len(itemList)):
    list = itemList[i]
    print(f"{i}. {list}")

