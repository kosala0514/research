import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

radius = 5
area = calculate_area(radius)
print("The area of the circle with radius", radius, "is:", area)
