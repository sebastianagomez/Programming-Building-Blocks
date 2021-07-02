print("For each of these questions, please provide a 1-10 rating:\n")

largeLoan = int(input("How large is your loan? "))

creditHistory = int(input("How good is your credit history? "))

income = int(input("How high is your income? "))

downPayment = int(input("How large is your down payment? "))

loan = False

if largeLoan >= 5:
    if creditHistory and income >= 7:
        loan = True
    elif creditHistory or income >= 7:
        if  downPayment >= 5:
            loan = True 
        else: 
            loan = False
    else:
        loan = False

else: 
    if creditHistory < 4:
        loan = False
    else:
        if income or downPayment >= 7:
            loan = True
        elif income and downPayment >= 4:
            loan = True
        else:
            loan = False

if loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")