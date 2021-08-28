"""
website requires the users to input username and password to register. Write a program to check the 
validity of password input by users.

    Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12

    Your program should accept a sequence of comma separated passwords and will check them according 
    to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

    Example

    If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

    Then, the output of the program should be:

ABd1234@1
"""
def low_case(p):
    for i in p:
        if 'a' <= i and 'z' >= i:
            return True
    return False

def num(p):
    for i in p:
        if '0' <= i and '9' >= i:
            return True
    return False

def up_case(p):
    for i in p:
        if 'A' <= i and 'Z' >= i:
            return True
    return False

def other(p):
    for i in p:
        if i == '$' or i == '#' or i == '@':
            return True
    return False
    
pass_word = input("Your pass: ").split(",")
lst = []

for i in pass_word:
    length = len(pass_word)
    if 6 <= length and 12 >= length and low_case(i) and up_case(i) and num(i) and other (i):
        lst.append(i)

print(",".join(lst))

