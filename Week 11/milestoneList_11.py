"""
File: milestoneList_11py
Author: Sebastian Gomez

Purpose: Write a program to analyze a dataset containing information about 
        life expectancies over the years throughout the countries of the world.
Date: 07/11/2021
"""

import math

minLifeExp = math.inf
minCountry = ""
minYear = None
maxLifeExp = 0
maxCountry = ""
maxYear = None
sumLifeExp = []
sumCount = []
totalNumbers = 0
maxSelectedCountry = ""
maxSelectedLifeExp = 0
minSelectedCountry = ""
minSelectedLifeExp = math.inf

print()
print("Welcome!")
print()

interestYear = int(input("Enter the year of interest: "))
with open("Week 11/life-expectancy.csv") as lifeExpectancyFile:
    lifeExpectancyFile.readline()
    for row in lifeExpectancyFile:
        lifeExpDivided = row.strip()
        lifeExpDivided = lifeExpDivided.split(",")
        years = int(lifeExpDivided[2])
        lifeExp = float(lifeExpDivided[3])
        countries = str(lifeExpDivided[0])
        if interestYear == years:
            sumLifeExp.append(lifeExp)
            count = years - years + 1
            sumCount.append(count)
            totalNumbers = sum(sumCount)
            totalLifeExp = sum(sumLifeExp)
            average = totalLifeExp / totalNumbers
            if lifeExp < minSelectedLifeExp:
                minSelectedLifeExp = lifeExp
                minSelectedCountry = countries
            elif lifeExp > maxSelectedLifeExp:
                maxSelectedLifeExp = lifeExp
                maxSelectedCountry = countries
        elif lifeExp < minLifeExp:
            minLifeExp = lifeExp
            minCountry = countries
            minYear = years
        elif lifeExp > maxLifeExp:
            maxLifeExp = lifeExp
            maxCountry = countries
            maxYear = years

print(f"\nThe overall max life expectancy is: {maxLifeExp} from {maxCountry} in {maxYear}")
print(f"The overall min life expectancy is: {minLifeExp} from {minCountry} in {minYear}")
print(f"\nFor the year {interestYear}: \nThe average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was {maxSelectedCountry} with {maxSelectedLifeExp}")
print(f"The min life expectancy was {minSelectedCountry} with {minSelectedLifeExp}")