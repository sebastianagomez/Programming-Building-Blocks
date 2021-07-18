"""
File: windChill_13py
Author: Sebastian Gomez

Purpose: Write a program that asks the user for a temperature and then shows the wind chill 
         values for various wind speeds at that temperature.
Date: 07/17/2021
"""

def Fahrenheit(T, V):
    windChill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V **0.16)
    return windChill

def Celsius(T):
    toFahrenheit = (T * 9/5) + 32
    return toFahrenheit 

temperature = "" 
quit= ""

while quit.upper() != "Y":
    temperature = float(input("What is the temperature? "))
    fahrOrCel = input("Fahrenheit or Celsius (F/C)? ")
    fahrOrCel = fahrOrCel.lower()    
    if fahrOrCel == "f":
        for x in range(5, 65 ,5):
            windChill = Fahrenheit(temperature, x)
            print(f"At temperature {temperature:.1f}°F, and wind speed {x} mph, the windchill is: {windChill:.2f}°F")
    elif fahrOrCel == "c":
         for x in range(5, 65 ,5):
            windChill = Fahrenheit(Celsius(temperature), x)
            print(f"At temperature {Celsius(temperature):.1f}°F, and wind speed {x} mph, the windchill is: {windChill:.2f}°C")
    quit = input("Do you want to quit? (Y/N) ")