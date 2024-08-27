#8.Take single character from user check if the ascii value of character is Even the print character.

char1 = input("Enter char : ")
if len(char1)== 1:
    ascii_value = ord(char1)
    if ascii_value % 2 == 0:
            print(char1)
        