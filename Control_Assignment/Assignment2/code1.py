#1. WAP to check numbers are divisible by 4 and 5 Print those numbers

num1= int(input("Enter number : "))
if(num1%4 ==0 and num1 % 5 == 0):
    print(num1,"is divisible by 4 and 5")
else : 
    print(num1,"is not divisible by 4 and 5")