# program1.WAP to print numbers from a given range.

# for i in range(100,110):
#      print(i,end= " ")



# program 2.WAP to print numbers from a given range.
# for i in range(10,20):
#      if(i%2 == 0):
#           print(i)

# program 3. Wap to print sum of all numbers from a given range
# sum = 0
# for num in range(1,10):
#      sum += num
# print(sum)



# program4.WAP to print all the character values of the given ASCII value range from the user

# start = int(input("Enter the start of range: "))
# end = int(input("Enter end of range: "))
# if start < 0 or end > 127 or start > end:
#             print("Wrong input")
# else:
#     for i in range(start, end + 1):
#         print(f"The character of ASCII value {i} is {chr(i)}.")



# program5.WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100 

# start = int(input("Enter start of range : "))
# end = int(input("Enter end of range : "))
# for i in range (1, 100):
#     if i%7 == 0 and i%3 !=0:
#         print(i)



# program6. WAP to print all the ASCII values from a given character range.

# start = 'A'
# end = 'Z'
# for char in range(ord(start), ord(end) + 1):
#     print(f"ASCII value of {chr(char)} is {char}")

# program6. WAP that prints all Positive numbers from a given range.

# for i in range(-7,8):
#     if i > 0:    
#         print(i)

# program7.WAP to prints numbers which are divisible by 3 and 5 both in a given range.

# for i in range(10,50):
#     if i %15 ==0:
#         print(i)


# WAP to print the count of all negative numbers from a given range
# start = int(input("Enter number : "))
# end = int(input("Enter number : "))
# count = 0
# for number in range(start, end+1):
#     if number < 0:
#         count += 1

# print("Count of negative numbers:",count)

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
count = 0
for number in range(start, end + 1):
    if number % 2 != 0:
        count += 1
product = 1
for _ in range(count):
    product *= count

print(product)
