from datetime import datetime

def printTime(taskName):
    print(taskName)
    print(datetime.now())
    print()

printTime('Sebastian')


# I can use a function, but this time my function returns a value

def getInitial(name, forceUppercase):
    if forceUppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

firstName = input("Enter your first name: ")
firstNameInitial = getInitial(firstName, False)

lastName = input("Enter your last name: ")
lastNameInitial = getInitial(lastName, False)

print("Your initials are: " + firstNameInitial + lastNameInitial)