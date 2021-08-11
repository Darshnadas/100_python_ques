"""
Find the Nth fibonacchi number in the fibonacci series
"""
x, y, sum = 0, 1, 0
n = int(input("Enter nth num: "))
for i in range(1, n+1):
    sum = x + y
    x = y
    y = sum
    if i == (n-1):
        print(f"Nth num is {x}")