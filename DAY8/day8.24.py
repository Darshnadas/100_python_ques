"""
Python has many built-in functions, and if you do not know how to use it, you can read document 
online or find some books. But Python has a built-in document function for every built-in functions.

    Please write a program to print some Python built-in functions documents, such as 
    abs(), int(), raw_input()

    And add document for your own function
"""
print(abs.__doc__)
print(int.__doc__)
print(str.__doc__)

def pow_num(n,p):
    '''
    Return square of an interger input
    '''
    return n**p

print(pow_num(4,2))
print(pow_num.__doc__)

