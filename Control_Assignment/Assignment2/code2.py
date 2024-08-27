#2. WAP to determine whether entered angles define a right-angled triangle. Take three values of angle from the user.

A1 = int(input("Enter angle1 : "))
A2 = int(input("Enter angle2 : "))
A3 = int(input("Enter angle3 : "))
if (A1== 90 or A2 == 90 or A3 == 90):
    if (A1 + A2 ==90 or A2 + A3 == 90 or A3 + A1==90):
        print(" is  right angle triangle")
    else :
        print("is not right angle tringle")
else :
    print("tringle is not right angle tringle")
