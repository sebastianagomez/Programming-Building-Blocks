int1 = int(input("The first number is: "))
int2 = int(input("The first number is: "))

if int1 > int2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if int1 == int2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if int2 > int1:
    print("The second number is greater")
else:
    print("The second number is not greater")

print()

animalUser = input("What is your favorite animal? ")
animal = "horse"

if animalUser.lower() == animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")