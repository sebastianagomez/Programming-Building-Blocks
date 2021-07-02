gradePer = float(input("What is your grade percentage? "))

if gradePer >= 90:
    letter = "A"
elif gradePer >= 80:
    letter = "B"
elif gradePer >= 70:
    letter = "C"
elif gradePer >= 60:
    letter = "D"
else:
    letter = "F"

formugradePer = gradePer % 10

if formugradePer >= 7:
    sign = "+"
elif formugradePer < 3:
    sign = "-"
else:
    sign = ""

if gradePer >= 93:
    sign = ""

if letter == "F":
    sign = ""

print("Your grade is " + str(letter) + sign)
if gradePer >= 70:
    print("Congratulations! Your pass the class.")
else:
    print("You can do it next time!")


    



