import math

square = float(input("What is the lenght of a side of the square? "))
formuSquare = square * square
print("The area of the square is: " + str(formuSquare))

print()

rectangleLen = float(input("What is the length of the rectangle? "))
rectangleWid = float(input("What is the width of the rectangle? "))
formuRectangle = rectangleLen * rectangleWid
print("The area of the triangle is: " + str(formuRectangle))

print()

circleRad = float(input("What is the radius of the circle? "))
formuCircleRad = 2 * math.pi * circleRad
formula = int(formuCircleRad)
print ("The radius of the circle is: " + str(formula))

print()
length = float(input("Prompt a single length value: "))
formuSquareArea = length * 4
formuCircle = length * math.pi * 2
formuCube = length ** 3
formuSphere = (4/3) * math.pi (length ** 3)
print(formuSquareArea)
print(formuCircle)
print(formuCube)
print(formuSphere)


