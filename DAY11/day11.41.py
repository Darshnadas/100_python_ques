"""
Write a program which can map() to make a list whose elements are square of elements in 
[1,2,3,4,5,6,7,8,9,10].

"""
def square(i):
    return i ** 2

num = [i for i in range(1,11)]
sq_lst = map(square, num)
print(list(sq_lst))