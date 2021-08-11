"""
Write a program that computes the net amount of a bank account based a transaction log from console 
input. The transaction log format is shown as following:

D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

Then, the output should be:
500
"""
acc = 0
while True:
    option = input("Deposit/Withdrawl/Balance? press d / w/ b / q(to quit): ").lower()

    if option == 'd':
        dep = input("Amount you would like to deposit?")
        acc = acc + int(dep)
    elif option == 'w':
        withdraw = input("Amount you would like to withdraw?")
        acc = acc - int(withdraw)
    elif option == 'b':
        print(acc)
    else:
        quit()