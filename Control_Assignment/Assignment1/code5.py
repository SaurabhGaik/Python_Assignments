# Program 5: Write a Program to take an integer ranging from 0 to 6 and print corresponding weekday (week starting from Monday)

print("Enter a number between 0 to 6 ")
num = int(input("Enter number : "))
if (num == 0) :
    print("monday")
elif(num == 1) :
    print("Tuesday")
elif(num == 2) :
    print("Wednesday")
elif(num == 3) :
    print("Thursday")
elif(num == 4) :
    print("Friday")
elif(num == 5) :
    print("Saturday")
elif(num == 6) :
    print("Sunday")
else :
    print("Invalid input number ")