"""
Note in the same program, I want you to calculate factorial by two methods. The first using a loop as
already noted. The second is using the math function factorial. The factorial function is in the math library
that you import into your program by using the statement

import math

Find the factorial function in that library (remember I told you how). To use the function, you type
something like

x = math.xxx(input_var)

Where xxx is the factorial function (hey, I am not going to give it to you-that would take all the fun out of
this problem).

Some comments. 0! = 1. Do not try big numbers. Don’t go any higher than 10!

Test with 0! = 1, 5! = 120.
____
In mathematics, the notation 𝑛! represents the factorial of the nonnegative integer 𝑛. The factorial of 𝑛 is
defined as the product of all the nonnegative integers from 1 to 𝑛. For example,

7! = 1×2×3×4×5×6×7 = 5,040

and

4! = 1×2×3×4 = 24

Write a program that lets the user enter a nonnegative integer (check for this) then uses a loop to calculate
the factorial of that number. Display the factorial.
"""
# Calculating the Factorial of a Number V1, Program 4-11 Textbook, Fri, Feb 16, 2025 6 PM
# Calculates the factorial of a number using custom code and the math.factorial() function
#
# Input
#   Non-Negative Int from user
#
# Output
#   Factorial of Input
#
# n! = n * ( n - 1 ) * ... * 1

# Libraries
import pyinputplus as pyip # Input Validation
import math # For Factorial Function

# Program
print(f"This program calculates the factorial of a number")

# User Input
n = pyip.inputInt("Enter a non negative Integer: ", min=0) # x! where x < 0 = undefined

# Calculates Factorial(n)
s = 1 # Init: solution, used in output
for i in range(1, n):
    s = s * (i+1)

# Output
print(f"Factorial {n} = {s}")
print(f"Factorial {n} = {math.factorial(n)} (math.factorial)")

print("End of Program")