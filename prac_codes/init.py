"""
Construct a class with init method
"""

class Student:
    def __init__(self,name,branch,year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A sudent object is created.")

    def print_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
std1 = Student('Darshna', 'ECE', '2021')
std2 = Student('Deshna', 'CSE', '2031')
std3 = Student('Sonia', 'IT', '1997')


std1.print_details()
std2.print_details()
std3.print_details()

