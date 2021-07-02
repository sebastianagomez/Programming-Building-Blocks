placeList = []
codeList = []
yearList = []
valueList = []

with open("Week 11/life-expectancy.csv") as database:
    database.readline()
    for line in database:
        data = line.split(",")
        placeList.append(data[0])
        codeList.append(data[1])
        yearList.append(data[2])
        valueList.append(float(data[3]))
    
    print(min(valueList))
    print(max(valueList))