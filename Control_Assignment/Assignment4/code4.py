# program4.WAP to print all the character values of the given ASCII value range from the user

start = int(input("Enter the start of range: "))
end = int(input("Enter end of range: "))
if start < 0 or end > 127 or start > end:
            print("Wrong input")
else:
    for i in range(start, end + 1):
        print(f"The character of ASCII value {i} is {chr(i)}.")