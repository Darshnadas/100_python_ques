"""
Calculate the average of N numbers.
"""
N = 10
sum = 0
count = 0
while count < N:
    num = float(input("Enter a num: "))
    sum = sum + num
    count = count + 1
avg = float(sum) / N
print("N = %d, Sum = %f" % (N,sum))
print("Average = %f" % avg)
