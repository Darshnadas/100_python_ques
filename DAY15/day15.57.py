"""
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

"""
s = input("Enter a string: ")
u = s.encode('utf-8')
print(u)