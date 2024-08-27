#3. Take two numbers from users and print the sum of those numbers if the sum is even.

num1 = int(input("Enter value : "))
num2 = int(input("Enter value : "))
sum = num1 + num2
if (sum %2 == 0):
    print(sum,"is even")