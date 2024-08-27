#9. Program 9: Write a program to check whether the input character is a vowel or consonants

char = input("Enter a chaaaracter : ")
if char in 'aeiouAEIOU' :
    print("vowel")
elif char.isalpha():
    print("consonant")
else :
     print(char, "is not an alphabetic character.")