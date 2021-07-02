number = float(input("Please type a positive number: "))

while number <= 0:
    print("Sorry this is a negative. Please try again.")
    number = float(input("Please type a positive number: "))

print(f"The number is: {number}")

# 2 task
print()

answer = input("May I have a piece of candy? ")

while answer == "no":    
    answer = input("May I have a piece of candy? ")
    if answer == "yes":
        print("Thank you.")
    else:
        answer = input("May I have a piece of candy? ")