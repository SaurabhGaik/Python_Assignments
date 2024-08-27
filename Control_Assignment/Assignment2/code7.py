# Take two numbers from the user, check if both are odd and then print the sum of the numbers.

num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
sum = num1 + num2
if(sum %2== 1):
    print(sum)
