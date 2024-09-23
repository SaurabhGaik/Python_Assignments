def parent_function():
    def myIndex(listData, searchEle):
        if searchEle in listData:
            return listData.index(searchEle)
        else:
            return -1
    def myPalindrome(num):
        return str(num) == str(num)[::-1]
    
    choice = int(input("Enter 1 to find index or 2 to check palindrome: "))

    if choice == 1:
        listData = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        searchEle = int(input("Enter the element to search: "))
        result = myIndex(listData, searchEle)
        print("Output:", result)
    elif choice == 2:
        num = int(input("Enter a number to check if it's a palindrome: "))
        result = myPalindrome(num)
        print("Output:", result)
    else:
        print("Invalid choice")

parent_function()
