# 10.Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.

num = int(input("Enter a number: "))
remainder = num % 8
if remainder == 3:
        print(remainder)
