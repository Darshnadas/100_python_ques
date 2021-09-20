"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" 
or "Yes", otherwise print "No".
"""

sentence = input("Enter anything you like: ")
if sentence == "Yes" or sentence == "YES" or sentence == "yes":
    print("Yes")
else:
    print("No")