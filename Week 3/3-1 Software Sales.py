"""
If you messed up with Magic Numbers on previous problems, 
this one is a chance for you to redeem yourself. 
Remember, every number in this problem is a Magic Number. 
Handle them appropriately.
Spend the time and do this problem correctly. 
You will see something similar on the upcoming exam.

A software company sells a package that retails for $99. 
Quantity discounts are given according to the following table:
-----------  --------  -----------------
Quantity     Discount  Interval Notation
10-19        10%       [10, 19]
20-49        20%       [20, 49]
50-99        30%       [50, 99]
100 or more  40%       [100, ∞)
-----------  --------  -----------------
Write a program that asks the user to enter the number of packages purchased. 
The program should then display the amount of the discount (if any) 
and the total amount of the purchase after the discount.
"""
# Software Sales V1, Program 3-12 Textbook, Fri, Feb 16, 2025 6 PM
# Calculates total cost based off quantities purchased, unit price, and pre-defined bulk discount ranges
#
# Input
#   # of Packages Purchased
#
# Output
#   Purchase Receipt
#
# -----------  --------  -----------------
# Quantity     Discount  Interval Notation
# 10-19        10%       [10, 19]
# 20-49        20%       [20, 49]
# 50-99        30%       [50, 99]
# 100 or more  40%       [100, ∞)
# -----------  --------  -----------------
#
# For Non-Discounted Items
#   Retail Price = Quantity * Unit Price
# For Discounted Items
#   Final Price = Retail Price - ( Retail Price * ( Discount% / 100 ) )

# Libraries
from collections import namedtuple # Unbounded Range Storage; praise be these are great, perfect in-between of tuples and dicts
from decimal import Decimal, ROUND_HALF_UP # Precise Decimal Handling
import pyinputplus as pyip # Input validation
from rich.console import Console # Fancy Output
from rich.table import Table # Fancy Output

# Globals
price_per_package: int = 99 # Unit Price; configurable

# Container allowing infinite range, Labels (+readability) 
DiscountRange = namedtuple(typename='DiscountRange', field_names=['min_qty', 'max_qty', 'discount_percentage'])

# Stores All Data Required for Calc
discount_ranges = (
    DiscountRange(min_qty=10, max_qty=19, discount_percentage=10),
    DiscountRange(20, 49, 20),
    DiscountRange(50, 99, 30),
    DiscountRange(100, float('inf'), 40) 
)

# Functions
# Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
def roundToCent(number: Decimal) -> Decimal: 
    return number.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# Program
print(f"This program calculates the total cost of packages")

# User Input
packages_purchased: int = pyip.inputInt("How many packages will you be purchasing? ", min=1)

# Calculates Prices
retail_price: int = packages_purchased * price_per_package # Finds Retail Price, Needed regardless of discount

# Determines Discount % & $, if any
discounted: bool = False # Init: discounted state, determines if discount info needed on receipt

for discount_range in discount_ranges: 
    if discount_range.min_qty <= packages_purchased <= discount_range.max_qty: # Is qty in current discount range?
        discount_percentage: int = discount_range.discount_percentage # discount_percentage to global; used in receipt 
        discounted_price: Decimal = retail_price - ( retail_price * ( Decimal(discount_percentage) / Decimal(100) ) ) # Calculates Discounted Price
        discounted = True
        break # Discount Range Found; Stops Searching

# Output
# Table Init, Always used columns
table = Table(title="Your Receipt")
table.add_column("QTY", justify="center")
table.add_column("$/unit", justify="right")

# Changes Receipt based on discounted status
if discounted: # Discounted Receipt
    table.add_column("List Price", justify="right")
    table.add_column("Bulk Discount", style="magenta italic")
    table.add_column("Final Price", justify="right", style="bold green")

    table.add_row(
        f"{packages_purchased}", 
        f"${price_per_package:.2f}", 
        f"${retail_price:,.2f}", 
        f"{discount_percentage}% off", 
        f"${roundToCent(discounted_price):,}"
    )
else: # Non-Discounted Receipt
    table.add_column("Final Price", justify="right", style="bold green")

    table.add_row(
        f"{packages_purchased}", 
        f"${price_per_package:.2f}", 
        f"${retail_price:,.2f}"
    )

console = Console()
console.print(table)

print("End of Program")