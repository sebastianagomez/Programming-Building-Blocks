tip = float(input("What is the tip amount? ")) 

while tip < 0:
    print("Sorry, the tip cannot be negative!")
    tip = float(input("What is the tip amount? ")) 

print(f"You have tipped an amount of {tip:.2f}")

# from PIL import Image
# print("The library is loaded correctly")