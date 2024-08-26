#1. WAP to check numbers are divisible by 4 and 5 Print those numbers

# num1= int(input("Enter number : "))
# if(num1%4 ==0 and num1 % 5 == 0):
#     print(num1,"is divisible by 4 and 5")
# else : 
#     print(num1,"is not divisible by 4 and 5")



#2. WAP to determine whether entered angles define a right-angled triangle. Take three values of angle from the user.

# A1 = int(input("Enter angle1 : "))
# A2 = int(input("Enter angle2 : "))
# A3 = int(input("Enter angle3 : "))
# if (A1== 90 or A2 == 90 or A3 == 90):
#     if (A1 + A2 ==90 or A2 + A3 == 90 or A3 + A1==90):
#         print(" is  right angle triangle")
#     else :
#         print("is not right angle tringle")
# else :
#     print("tringle is not right angle tringle")


#3. Take two numbers from users and print the sum of those numbers if the sum is even.

# num1 = int(input("Enter value : "))
# num2 = int(input("Enter value : "))
# sum = num1 + num2
# if (sum %2 == 0):
#     print(sum,"is even")


#4 Take a number from the user and check whether it is present in the list. If it's in the list, print "Available."


# list1 = [10, 20, 30, 40, 50]
# num = int(input("Enter number : "))
# if num in list1:
#         print("Available")



#5.Print the "Core2web" string a number of times entered by the user if the number is even.

# num = int(input("Enter number : "))
# if num %2 == 0:
#     print("number is even")
#     for _  in range(num) :
#         print("core2web")


#6. Write a program that checks if a given number is odd using the "if" statement.

# num = int(input("Enter number : "))
# if (num %2 == 1):
#     print(num,"is odd")

# Take two numbers from the user, check if both are odd and then print the sum of the numbers.

# num1 = int(input("Enter number : "))
# num2 = int(input("Enter number : "))
# sum = num1 + num2
# if(sum %2== 1):
#     print(sum)


#8.Take single character from user check if the ascii value of character is Even the print character.

# char1 = input("Enter char : ")
# if len(char1)== 1:
#     ascii_value = ord(char1)
#     if ascii_value % 2 == 0:
#             print(char1)
        

#9. Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character

# char1 = input("Enter char : ")
# char2 = input("Enter char1 : ")
# ascii1 = ord(char1)
# ascii2 = ord(char2)
# if ascii1 %2 != 0 and ascii2 %2 != 0 :
#     print(ascii1 + ascii2)



# 10.Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.

num = int(input("Enter a number: "))
remainder = num % 8
if remainder == 3:
        print(remainder)

