#9. Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character

char1 = input("Enter char : ")
char2 = input("Enter char1 : ")
ascii1 = ord(char1)
ascii2 = ord(char2)
if ascii1 %2 != 0 and ascii2 %2 != 0 :
    print(ascii1 + ascii2)
