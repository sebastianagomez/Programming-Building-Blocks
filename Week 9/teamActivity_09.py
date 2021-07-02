numberList = []

newNumber = None

listLength = 0

while newNumber != 0:
    newNumber = float(input("Enter a number: "))
    if newNumber != 0:
        numberList.append(newNumber)
        listLength += 1

print(sum(numberList))
print(sum(numberList)/listLength)
print(max(numberList))
print(min(item for item in numberList if item > 0))       


