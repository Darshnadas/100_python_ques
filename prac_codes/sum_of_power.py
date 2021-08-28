"""
Write a program where you will calculate the sum of power of digits of the number given by user.
"""
lst = []
n = int(input())
while n > 0:
    lst.append(n % 10)
    n = n // 10
lst.reverse()
p = len(lst)
sum = 0

for i in range(p-1):
    sum = sum + pow(lst[i], lst[i + 1])

print(sum + 1)