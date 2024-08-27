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
