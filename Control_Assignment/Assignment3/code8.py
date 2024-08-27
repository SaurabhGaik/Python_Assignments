#8.Write a program to print a table of 12 in reverse order

number = 12
for i in range(10,0,-1):
    result = number * i
print(f"{number} x {i} = {result}")