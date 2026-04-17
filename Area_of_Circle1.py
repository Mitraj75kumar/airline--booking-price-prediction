def Area_Of_Circle(Radius):
    pi = 3.14
    Area = pi * Radius**2
    return Area
Radius = int(input("Enter a radius: "))
result = Area_Of_Circle(Radius)
print("Area of Circle is: ", result)