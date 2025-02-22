"""
## Program 3-13 Shipping Charges
**Prof's Notes**: *Assume charge is calculated for individual packages and not for a combined weight of packages. For
example, if you have 5 packages 2# each, you would charge for each package. You would not charge the
rate for 10# for all the packages.*

**Problem** (pg200)
Write a program that asks the user to enter the weight of a package then displays the shipping charges.
"""
# Shipping Charges V1, Program 3-13 Textbook, Mon, Feb 10, 2025 6 PM
# Calculates Shipping Charges for a package based on pre-defined rates
#
# Input
#   Weight of Package from user (In lbs)
#
# Output
#   Shipping Charges Receipt
#
# Shipping Rates as of Feb 6th, 2025
# -------------------------------------  --------------  -----------------
# Weight of Package                      Rate per Pound  Interval Notation
# 2 lbs. or less                         $1.50           [0, 2]
# Over 2 lbs. but not more than 6 lbs.   $3.00           (2, 6]
# Over 6 lbs. but not more than 10 lbs.  $4.00           (6, 10]
# Over 10 lbs.                           $4.75           (10, ∞)
# -------------------------------------  --------------  -----------------
#
# Total Cost Calculation
# Total Cost = Rate per Pound * Package Weight (lbs)

# Libraries
from decimal import Decimal, ROUND_HALF_UP # Precise Decimal Handling
import pyinputplus as pyip # Input validation
from tabulate import tabulate # Table Formatted Output

# Globals
S_package_max_weight = 2
M_package_max_weight = 6
L_package_max_weight = 10 # Also XL_package_min_weight (exclusive), although there is no current use for the variable

S_price_per_pound = Decimal("1.50")
M_price_per_pound = Decimal("3")
L_price_per_pound = Decimal("4")
XL_price_per_pound = Decimal("4.75")

# Functions
def roundToCent(number: Decimal): # Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
    return number.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# Program
print(f"This program calculates the shipping charges of a package based on it's weight")

# User Input
package_weight = pyip.inputFloat("Please input the weight of your package in pounds (lbs): ", min=0) # minimum = 0; If your weight is negative contact a physicist 
package_weight = Decimal(str(package_weight)) # Decimal Object requires a str input for precision

# Finds Weight Class 
if package_weight <= S_package_max_weight:
    package_class = "Small"
    price_per_pound = S_price_per_pound
elif package_weight <= M_package_max_weight:
    package_class = "Medium"
    price_per_pound = M_price_per_pound
elif package_weight <= L_package_max_weight:
    package_class = "Large"
    price_per_pound = L_price_per_pound
else:
    package_class = "Extra Large"
    price_per_pound = XL_price_per_pound

# Calculates Total
total_price = package_weight * price_per_pound

# Output
package_receipt = [
    ["Package Class", "Package Weight", "$/lb", "Total Price"],
    [package_class, f"{package_weight} lbs", f"${price_per_pound}", f"${roundToCent(total_price)}"]
] 
print(tabulate(package_receipt))

print("End of Program")