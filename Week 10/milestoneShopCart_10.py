"""
File: ProveAssignment_10py
Author: Sebastian Gomez

Purpose: Practicing with list indexes.
Date: 06/26/2021
"""

print("Welcome to the Shopping Cart Program!")

required = "\n\nPlease enter again you answer\n\n"

itemList = []
itemPriceList = []

newItem = ""
itemPrice = ""


def intro():
    print("\nPlease select one of the following:  \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
    choice = input("\nPlease enter an action: ")
    if choice == "1":
        AddItem()
    elif choice == "2":
        ViewCart()
    elif choice == "3":
        RemoveItem()
    elif choice == "4":
        ComputeTotal()
    elif choice == "5":
        Quit()
    else:
        print(required)
        intro()

def AddItem():
    newItem = input("\nWhat item would you like to add? ")
    itemList.append(newItem)
    itemPrice = float(input(f"What is the price of '{newItem}'? "))
    itemPriceList.append(itemPrice)
    print(f"'{newItem}' has been added to the cart.")
    intro()

def ViewCart():
    print()
    print("The contents of the shopping cart are:")
    print()

    for i in range(len(itemList)) and range(len(itemPriceList)):
        list = itemList[i]
        price = itemPriceList[i]
        print(f"{i+1}. {list} - ${price:.2f}")
    intro()

def RemoveItem():
    changeItem = int(input("\nWhich number of item would you like to remove? "))
    if  changeItem < 1 or changeItem >len(itemList):
        print("Sorry, that is not a valid item number.")
        RemoveItem()
    else:
        itemList.pop(changeItem-1)
        itemPriceList.pop(changeItem-1)
        print("Item removed.")
    intro()

def ComputeTotal():

    totalAmount = sum(itemPriceList)
    print(f"\nThe total price of the items in the shopping cart is ${totalAmount:.2f}")

    print("\nIf you answer this question you will have a 15% discount:")
    questionDiscount = input("\nIn what year was the first vision? ")
    if questionDiscount == "1820":
        discount = totalAmount * 0.15
        formuTotal = totalAmount - discount
        print("\nCongrats! You got the discount!\n")
        print(f"The total price of the items in the shopping cart is ${formuTotal:.2f}")
    else:
        print("Sorry, that was not the answer... Maybe later.")     

    intro()

def Quit():
    print("Thank you. Goodbye.")

intro()
