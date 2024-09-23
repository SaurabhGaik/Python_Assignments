#WAP for function return the array of factrial of the elememt
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_array(arr):
    return [factorial(x) for x in arr]

input = [1, 2, 3, 4, 5]
output = factorial_array(input)
print(output)  # Output: [1, 2, 6, 24, 120]

