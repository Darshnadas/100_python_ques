"""
Write a program which can filter() to make a list whose elements are even number between 1 and 20 
(both included).
"""

def even(i):
    return (i%2 == 0)

num = filter(even, range(1,21))
print(list(num))