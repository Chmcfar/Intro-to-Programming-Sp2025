# Tuition Increase V1, Exam 1, Problem 3, Sun, Feb 23, 2025 6PM
# Approximates cost of semester tuition based on starting amount, annual growth percentage, time
#
# Input - Pre-Defined Globals
#   Starting Tuition
#   Annual Tuition Increase Percentage
#   Total Projection Years
#
# Output
#   Formatted table of: years, approximated semester tuition
#
# Compound Interest Formula 𝐴 = 𝑃(1 + (𝑟/𝑛) )^(𝑛𝑡)

# Libraries
from decimal import Decimal, ROUND_HALF_UP # Precise Decimal Handling
from rich.console import Console # Fancy Output
from rich.table import Table # Fancy Output

# Globals
tuition_per_semester : Decimal = Decimal(9_500) 
annual_tuition_increase_percentage: int = 3
years_projected: int = 10

# Functions
# For Output Formatting: Align on decimal point via padding
def alignToDecimal(numbers: list[str]) -> list[str]: 
    # Helper Func for Padding Calc
    def intLen(num: str) -> int: # Returns len of int part of deci
        return len(num.split(".")[0])
    
    max_left_pad: int = max(intLen(str(num)) for num in numbers) # Determines Max Padding
    padded_numbers: list[str] = [] # Init: Padded Numbers Return Container

    # Pads nums, appends to return list
    for num in numbers:
        num_len: int = intLen(num)

        if num_len < max_left_pad: # Check: Does current num needs padding?
            padding: int = max_left_pad - num_len 
            padded_numbers.append((" "*padding)+num) # Determine & Add padding, Append
        else:
            padded_numbers.append(num) # Append Un-padded nums
    return padded_numbers

# Replacement for pythons in-built rounding function (The latter is imprecise when dealing with floats)
def roundToCent(number: Decimal) -> Decimal: 
    return number.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# Convert applicable types to Decimal
def toDecimal(number: int | float | str) -> Decimal: 
    if isinstance(number, float): # float spec. case
        return Decimal(str(number)) # Ensure prec
    return Decimal(number)

# Self-Explanatory 
def compoundInterest(P: int | Decimal, r: int, n: int, t: int | Decimal) -> Decimal:
    return P * ( ( 1 + ( Decimal(r) / Decimal(100) ) ) ** ( n * t ) )

# Program
console = Console()
console.print(f"This program approximates the tuition costs per semester over time from pre-determined parameters", style="green")

# Calculates and saves Tuitions
tuition_counts: list[str] = [] # Collects all final tuitions for each year, used in output
tuition: Decimal = Decimal(tuition_per_semester) 
for year in range(1, years_projected+1):
    tuition_counts.append(f"${roundToCent(tuition):,}")
    tuition: Decimal = compoundInterest(
        P=tuition, 
        r=annual_tuition_increase_percentage, 
        n=1, 
        t=1
    )

# Output
table = Table()
console.print(f"Starting Semester Tuition: ${tuition_per_semester:,.2f}, increasing at {annual_tuition_increase_percentage}% per year for {years_projected} years")

# Table Init
table.add_column("Year")
table.add_column("Tuition Per Semester", justify="default")

for year, tuitions in enumerate(alignToDecimal(tuition_counts)):
    table.add_row(str(year+1), str(tuitions))

console.print(table)

console.print("End of Program", style="red")