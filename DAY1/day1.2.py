"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
f = 1
n = int(input("Enter a number as your choice: "))
for i in range(1,n+1):
    f = f * i
print(f, end =',')
