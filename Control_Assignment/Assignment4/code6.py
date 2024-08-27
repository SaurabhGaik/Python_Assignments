# program6. WAP to print all the ASCII values from a given character range.

start = 'A'
end = 'Z'
for char in range(ord(start), ord(end) + 1):
    print(f"ASCII value of {chr(char)} is {char}")
