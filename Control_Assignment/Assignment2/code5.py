#5.Print the "Core2web" string a number of times entered by the user if the number is even.

num = int(input("Enter number : "))
if num %2 == 0:
    print("number is even")
    for _  in range(num) :
        print("core2web")