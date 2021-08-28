"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a 
given range 0 and n.

    Suppose the following input is supplied to the program:

7

    Then, the output should be:

0
7
14
"""

class Div_num():
    def gen(self,n):
        for i in range(0,n):
            if i % 7 == 0:
                yield i

generate = Div_num()               
n = generate.gen(int(input("Enter a number: ")))
for i in n:
    print(i)


