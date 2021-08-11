"""

Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:

hello world! 123

    Then, the output should be:

LETTERS 10
DIGITS 3
"""
c1, c2 = 0, 0
sen = input("A sentence: ")
for i in sen:
    if i.isalpha():
        c1 += 1
    elif i.isnumeric():
        c2 += 1
print(f"LETTERS {c1}\nDIGITS {c2}")