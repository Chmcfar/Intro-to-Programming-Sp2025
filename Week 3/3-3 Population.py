"""
Do as the problem states. Limit it to no more than 20 days. 
Limit the print out to 4 decimal places ALIGNED on the decimal point 
(you may have to research this).

Write a program that predicts the approximate size of a population of organisms. 
The application should prompt the user to enter the starting number of organisms,
the average daily population increase (as a percentage), 
and the number of days the organisms will be left to multiply. 
For example, assume the user enters the following values:

Starting number of organisms: 2

Average daily increase: 30%

Number of days to multiply: 10

The program should display the following table of data:
--  --------
 1   2
 2   2.6
 3   3.38
 4   4.394
 5   5.7122
 6   7.42586
 7   9.65362
 8  12.5497
 9  16.3146
10  21.209
--  --------
"""
# Population V1, Program 4-12 Textbook, Fri, Feb 16, 6 PM
# Approximates size of populations based on starting amount, growth factor, time
#
# Input
#   Starting number of organisms
#   Average daily increase as percentage
#   Number of days to multiply
#
# Output
#   Formatted table of: days, approximated population
#
# Final Pop = Starting Pop + ( Starting Pop * ( Growth Percentage / 100 ) )

# Libraries
from decimal import Decimal, ROUND_HALF_UP # Precise Decimal Handling
import pyinputplus as pyip # Input validation
from rich.console import Console # Fancy Output
from rich.table import Table # Fancy Output

# Functions
# For Output Formatting: Align on decimal point via padding #! THIS FUNCTION WAS THE DEATH OF ME 
def alignToDecimal(numbers: list[Decimal]) -> list[str]: 
    # Helper Func for Padding Calc
    def intLen(num: str) -> int: # Returns len of int part of deci
        return len(num.split(".")[0])
    
    max_left_pad: int = max(intLen(str(num)) for num in numbers) # Determines Max Padding
    padded_numbers: list[str] = [] # Init: Padded Numbers Return Container

    # Cleans Trailing 0's and decis, pads nums, appends to return list
    for num in numbers:
        num: str = str(num)
        num_len: int = intLen(num)
        if num.endswith("0"): # Strips trailing 0's
            num = num.rstrip("0")
        if num.endswith("."): # Strips trailing .'s
            num = num.rstrip(".")

        if num_len < max_left_pad: # Check: Does current num needs padding?
            padding: int = max_left_pad - num_len 
            padded_numbers.append((" "*padding)+num) # Determine & Add padding, Append
        else:
            padded_numbers.append(num) # Append Un-padded nums
    return padded_numbers

# Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
def roundToTenThousandths(number: Decimal) -> Decimal: # Req: round 4 deci
    return number.quantize(Decimal('.0001'), rounding=ROUND_HALF_UP)

# Convert applicable types to Decimal
def toDecimal(number: int | float | str) -> Decimal: 
    if isinstance(number, float): # float spec. case
        return Decimal(str(number)) # Ensure prec
    return Decimal(number)

# Program
print(f"This program approximates size of populations given: starting pop., growth, and time")

# User Input
organism_count: Decimal = toDecimal(pyip.inputNum("Starting Number of Organisms: ", min=1))
daily_increase: Decimal = toDecimal(pyip.inputNum("Average Daily Increase Percentage: ", min=1))
days_to_multiply: int = pyip.inputInt("Days Left to Multiply: ", min=1, max=20) # Req: No more than 20 days

# Calculates and saves Final Pop's
organism_counts: list[Decimal] = [] # Collects all final pop's for each day, used in output

for day in range(1, days_to_multiply+1):
    organism_counts.append(roundToTenThousandths(organism_count))
    organism_count = organism_count + (organism_count * (daily_increase / Decimal(100) ) )

# Output
console = Console()
table = Table()

# Table Init
table.add_column("Day")
table.add_column("Organism Count", justify="default")

for day, organism_count in enumerate(alignToDecimal(organism_counts)): 
    table.add_row(str(day+1), str(organism_count))

console.print(table)

print("End of Program")