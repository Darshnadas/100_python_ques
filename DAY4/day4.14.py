"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case
letters.

    Suppose the following input is supplied to the program:

Hello world!

    Then, the output should be:

UPPER CASE 1
LOWER CASE 9
"""
up, low = 0, 0
sen = input("Enter a sentence: ")

for i in sen:
    if i >= 'A' and i <= 'Z':
        up += 1
    elif i >= 'a' and i <= 'z':
        low += 1
print(f"Uppercase {up}\nLowercase {low}")
