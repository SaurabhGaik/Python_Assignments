#7: Write a Program to take a number of months and print the number of days in that month.

month = int(input("Enter the month number (1-12): "))
if month == 1:
    month_name = "January"
    days = 31
elif month == 2:
    month_name = "February"
    days = 28 
elif month == 3:
    month_name = "March"
    days = 31
elif month == 4:
    month_name = "April"
    days = 30
elif month == 5:
    month_name = "May"
    days = 31
elif month == 6:
    month_name = "June"
    days = 30
elif month == 7:
    month_name = "July"
    days = 31
elif month == 8:
    month_name = "August"
    days = 31
elif month == 9:
    month_name = "September"
    days = 30
elif month == 10:
    month_name = "October"
    days = 31
elif month == 11:
    month_name = "November"
    days = 30
elif month == 12:
    month_name = "December"
    days = 31
else:
    month_name = "Invalid month"
    days = None  # Not applicable

print(month_name, "is a", days, "-day month.")