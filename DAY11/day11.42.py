"""
Write a program which can map() and filter() to make a list whose elements are square of even 
number in [1,2,3,4,5,6,7,8,9,10].
"""
def even(i):
    return i % 2 == 0

def sq(i):
    return i ** 2

num = [i for i in range(1,11)]
num = map(sq, filter(even, num))
print(list(num))