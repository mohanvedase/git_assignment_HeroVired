import math

class Calculator:
    def add(self, a, b): 
        return a + b
    def subtract(self, a, b): 
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b): 
         if b ==0:
            raise ValueError("Cannot divide by zero")
         return a/b  

if "__name__" == "__main__":
    calculator = Calculator()
num1 = 16
num2 = 4


calculator = Calculator()

print(f"{num1} + {num2} = {calculator.add(num1, num2)}") 
print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")