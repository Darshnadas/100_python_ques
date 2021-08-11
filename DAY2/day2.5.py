"""

Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.

Hints:

    Use init method to construct some parameters
"""
class String:
    def get_String(self):
        self.s = input()
    
    def print_string(self):
        print(self.s.upper())

op = String()
op.get_String()
op.print_string()