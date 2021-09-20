"""
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 
(both included).
"""
def sq_num(i):
    return i ** 2

num = map(sq_num, range(1,21))
print(list(num))
