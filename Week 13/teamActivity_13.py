import math

def computeAreaSquare(side):
    return side * side

def computeAreaRectangle(length, width):
    return length * width

def computeAreaCircle(radius):
    return math.pi * (radius * radius)  

shapeUser = "" 

while shapeUser != "quit":
    shapeUser = input("Shape you have: ")
    shapeUser = shapeUser.lower()

    if shapeUser == "square":
        sideUser = float(input("Side of the square: "))
        area = computeAreaSquare(sideUser)
        print(f"The area is {area}")
    elif shapeUser == "rectangle":
        lengthUser = float(input("Length of the rectangle: "))
        widthUser = float(input("Width of the rectangle: "))
        area = computeAreaRectangle(lengthUser, widthUser)
        print(f"The area is {area}")
    elif shapeUser == "circle":
        radiusUser = float(input("Radius of the circle: "))
        area = computeAreaCircle(radiusUser)
        print(f"The area is {area}")