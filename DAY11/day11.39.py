"""
Write a program to generate and print another tuple whose values are even numbers in the given 
tuple (1,2,3,4,5,6,7,8,9,10).
"""
lst = []

for i in range(1,11):
    if (i % 2 == 0):
        lst.append(i)
print(tuple(lst))

