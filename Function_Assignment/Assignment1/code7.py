
class Sum:
    def mySum(self, num1, num2):  # Method to sum two numbers
        return num1 + num2
# Creating two objects and getting user input
obj1 = Sum()
obj2 = Sum()
num1_1, num2_1 = int(input("Object 1 - Num1: ")), int(input("Object 1 - Num2: "))
num1_2, num2_2 = int(input("Object 2 - Num1: ")), int(input("Object 2 - Num2: "))
total_sum = obj1.mySum(num1_1, num2_1) + obj2.mySum(num1_2, num2_2)

# Output
print(f"Sum is {'Even' if total_sum % 2 == 0 else 'Odd'} {total_sum}")
