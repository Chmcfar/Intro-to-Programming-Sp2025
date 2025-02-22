# Compound Interest Calculator V1, Program 2-14 Textbook, Sun, Feb 2, 2025 6 PM
# Calculates Compound Interest given required variables from user
# 
# Input
#   Principal originally deposited into the account - User Input
#   Annual interest rate paid by the account - User Input
#   Times per year that the interest is compounded - User Input
#   Years the account will be left to earn interest - User Input
# 
# Output
#   Amount acuminated (𝐴) after 𝑡 years
#
# Compound Interest Formula 𝐴 = 𝑃(1 + (𝑟/𝑛) )^(𝑛𝑡)

# Libraries
import pyinputplus as pyip # Used for data validation
from decimal import Decimal, ROUND_HALF_UP # Used for decimal handling instead of floats (converting floats to ints for operations is possible but tedious)

# Functions
def roundToCent(number): # Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
    return number.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# Program
print("This program calculates the compound interest given \n - principle (𝑃) \n - an annual interest rate percentage (𝑟) \n - annual compound quantity (𝑛) \n - years of accumulation (𝑡)\n")

# User Input
# Decimal Object requires a str input for precision
principal = Decimal(str(pyip.inputNum("What is your Principle amount? $", min=0)))
r_annual_interest_rate_percent = Decimal(str(pyip.inputNum("What is your annual interest rate as percentage? ", min=0))) 
n_annual_compound_quantity = Decimal(str(pyip.inputNum("How many time a year does your interest compound in a year? ", min=1))) # min of 1 prevents DivBy0 error
t_years_of_accumulation = Decimal(str(pyip.inputNum("How many years will interest accumulate? ", min=0)))

r_annual_interest_rate = Decimal(str(r_annual_interest_rate_percent/100)) # Converts from % to decimal to be used in formula

# Calculation
amount = principal * ((1 + (r_annual_interest_rate/n_annual_compound_quantity) ) ** (n_annual_compound_quantity * t_years_of_accumulation))

# Output
print(f"After {t_years_of_accumulation} year(s) of accumulation you will have ${roundToCent(amount)}")
print("Program End")