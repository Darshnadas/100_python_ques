"""
Calculate investment
"""
amount = float(input("Enter an amount: "))
inrate = float(input('Enter your interest rate: '))
period = int(input("Enter period: "))

value = 0
year = 1

while year <= period:
    value = amount + (inrate * amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1
