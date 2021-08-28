"""
Input numbers into an array and add 2 to even numbers and 1 to odd numbers. Also count number of 
elements in the list.
"""
lst = []
c, p = 0,0

while True:
    n = input().split(',')
    if not n[0]:
        break
    for i in n:
        if int(i) % 2 == 0:
            lst.append(int(i) + 2)
            c += 1
        elif int(i) % 2 != 0:
            lst.append(int(i) + 3)
            p += 1
print(lst)
print("The number of elements in the list are", c + p)
