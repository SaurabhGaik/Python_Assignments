def analyzeNumber(num):
    def digitCount(n):
        return len(str(n))
    def evenDigitCount(n):
        return sum(1 for digit in str(n) if int(digit) % 2 == 0)
    def oddDigitCount(n):
        return sum(1 for digit in str(n) if int(digit) % 2 != 0)
    total = digitCount(num)
    even = evenDigitCount(num)
    odd = oddDigitCount(num)
    
    return [total, even, odd]


num = 12345
result = analyzeNumber(num)
print(result)  # Output: [5, 2, 3]
