# Tip, Tax, and Total V1, Program 2-8 Textbook, Sun Feb 2, 2025 6 PM
# Calculates Total owed for a meal given the cost of the meal by the user, 7% Sales Tax, and 18% Tip 
# 
# Input
#   Cost of meal/subtotal from user (Assumed Dollars)
# 
# Output
#   Subtotal, Sales Tax, Tip, Total (Assumed Dollars)

# Libraries
import pyinputplus as pyip # Input validation
from decimal import Decimal, ROUND_HALF_UP # Used for decimal handling instead of floats (converting floats to ints for operations is possible but tedious)

# Globals
sales_tax_percentage = 7
tip_percentage = 18

# Functions
def roundToCent(number): # Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
    return number.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# Program
print(f"This program calculates the total owed for a meal, given a sales tax of {sales_tax_percentage}% and tip of {tip_percentage}%")

# User input
charge = pyip.inputNum("Enter Charge for Food: $", min=0) # minimum = 0; You'll usually never be owed money for a getting meal 
subtotal = Decimal(str(charge)) # Decimal Object requires a str input for precision

# Calculates Tax, Tip and Total
tax = subtotal * (Decimal(str(sales_tax_percentage/100)))
tip = subtotal * (Decimal(str(tip_percentage/100)))
total = subtotal + tax + tip

# Output
print(f"Subtotal ${roundToCent(subtotal)}")
print(f"Sales Tax ({sales_tax_percentage}%) ${roundToCent(tax)}")
print(f"Tip ({tip_percentage}%) ${roundToCent(tip)}")
print(f"Total ${roundToCent(total)}")

print("End of Program.")
