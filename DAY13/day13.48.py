"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class 
has a method which can compute the area.
"""

class Rectangle():
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

l = int(input("Enter a length: "))
b = int(input("Enter a breadth: "))

rect = Rectangle(l,b)
print("The area is", rect.area())

