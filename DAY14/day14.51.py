"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def func():
    return 5/0

try:
    func()
except ZeroDivisionError as e:
    print("You  cannot divide a number by 0")
