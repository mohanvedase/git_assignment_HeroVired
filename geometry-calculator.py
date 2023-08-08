import math
class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
if "__name__" == "__main__": 
    calculator = GeometryCalculator()
 
radius = 5
calculator = GeometryCalculator()

print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
