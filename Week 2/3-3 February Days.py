"""
## Program 3-15 Leap Year Determination / February Days
**Prof's Notes**: *This is the easiest program of the homework! You can use 28 & 29 as constants. Assume they are not
magic numbers because everybody knows them.*

**Problem** (pg200)
The month of February normally has 28 days. But if it is a leap year, February has 29 days. Write a program that asks the user to enter a year. The program should then display the number of days in February that year. Use the following criteria to identify leap years:

1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.

Here is a sample run of the program:
```
Enter a year: 2008 [Enter] 
In 2008 February has 29 days.
```
"""
# February Days V1, Program 3-15 Textbook, Mon, Feb 10, 2025 6 PM
# Gives the amount of days in the February for the corresponding Gregorian calender year
#
# Input
#   Any Year during or after 1582 AD from user
#
# Output
#   The amount of days in February for the corresponding year

# Libraries
import pyinputplus as pyip # Input validation

# Program
print(f"This program determines if a year is a leap year")

# User Input
print("\033[33m"+"NOTE: This program only works for the years on the Gregorian Calender, which was implemented in 1582 AD \n  Previous years will not be accurate"+"\033[0m")
year = pyip.inputInt("Enter a year during or after 1582 AD: ", min=1582) # Acuate Results for the Gregorian Calender only

# Calculates Leap Year Status
if year % 100 == 0:
    if year % 400 == 0:
        feb_days = 29
    else:
        feb_days = 28
elif year % 4 == 0:
    feb_days = 29
else:
    feb_days = 28

# Output
print(f"In {year} AD, February had {feb_days} days")

print("End of Program")