"""
Define a function that can accept two strings as input and print the string with maximum length in 
console. If two strings have the same length, then the function should print all strings line by line.
"""

def length(l1,l2):
    if len(l1) > len(l2):
        print("The maximum length is of this string: ",l1)
    if len(l1) < len(l2):
        print("The maximum length is of this string: ",l2)
    elif len(l1) == len(l2):
        print("Same length:", l1, l2)

l1 = input("Enter a line-")
l2 = input("Enter 2nd line- ") 

print(length(l1,l2))