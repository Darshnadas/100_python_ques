"""
Define a custom exception class which takes a string message as attribute.
"""

class CustomException(Exception):
    """
    Exception raised for custom

    message --> explanation of the error raised
    """
    def __init__(self, msg):
        self.msg = msg
num = int(input())

try:
    if num < 10:
        raise CustomException("The input is less then 10")

    elif num > 10:
        raise CustomException("The input is greater than 10")

except CustomException as e:
    print("The error is raised: " + e.msg)
