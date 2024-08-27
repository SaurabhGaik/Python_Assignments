#Program 2: Write a Program to check whether the number is Negative,Positive or equal to Zero.

num = int(input("Enter value for num : "))
if (num > 0 ):
    print("{} is positive number".format(num))
elif(num < 0):
    print("{} is negative number".format(num))
else:
    print("number is zero")