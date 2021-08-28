"""
Define a function which can generate and print a list where the values are square of numbers 
between 1 and 20 (both included).
"""
def lst_sq():
    lst = [i ** 2 for i in range(1,21)]
    print(lst)

lst_sq()
