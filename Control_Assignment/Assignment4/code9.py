# WAP to print the count of all negative numbers from a given range

start = int(input("Enter number : "))
end = int(input("Enter number : "))
count = 0
for number in range(start, end+1):
    if number < 0:
        count += 1