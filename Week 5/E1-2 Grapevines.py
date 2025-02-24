# Grapevines V1, Exam 1, Problem 2, Sun, Feb 23, 2025 6PM
# Calculate the number of vines that will fit into a row, factoring in: end posts, and spacing
#
# Input
#   𝑅  =  the length of the row, in feet. 
#   𝐸  =  the amount of space, in feet, used by an end-post assembly. 
#   𝑆  =  the space between vines, in feet. 
#
# Output
#   𝑉  =  the number of grapevines that will fit in the row. 
#
# 𝑉 = ( 𝑅 − ( 2 × 𝐸 ) ) / 𝑆 

# Libraries
from decimal import Decimal # Precise Decimal Handling
import pyinputplus as pyip # Input Validation
from rich.console import Console # Fancy Output
from rich.table import Table # Fancy Output

# Functions
# Convert applicable types to Decimal
def toDecimal(number: int | float | str) -> Decimal:
    if isinstance(number, float): # float spec. case
        return Decimal(str(number)) # Ensure prec
    return Decimal(number)

# Program
console = Console()
console.print(f"This program calculates how many grapevines will fit in a row.", style="green")

# User Input # todo underline referenced object for clarity?
R_row_length: Decimal = toDecimal(pyip.inputNum("What is the length the row, in feet? ", min=.08)) 
E_post_length: Decimal = toDecimal(pyip.inputNum("What is the length used by an end-post assembly, in feet? ", min=.08)) 
S_vines_spacing: Decimal = toDecimal(pyip.inputNum("What is the length of space between vines, in feet? ", min=.08))  
# Min = .08 (ft) = ~1in; Technically min could be: anything > 0, but I don't think miniatures are applicable to this context

# Calculates Grapevine Capacity if parameters are valid
useable_row_length: Decimal = R_row_length - ( 2 * E_post_length )
feasible: bool = False
if E_post_length * 2 >= R_row_length:
    console.print(f"[bold red]Both End Assemblies take up the entire row [/bold red] {R_row_length}' (Row Length) ≤ {E_post_length*2}' (End Assembly × 2)")
elif useable_row_length < S_vines_spacing:
    console.print(f"[bold red]Vine Spacing is bigger than Useable Row Length[/bold red] {useable_row_length}' (Row Length) < {S_vines_spacing}' (Vine Spacing)")
else:
    V_grapevine_capacity: int = int(useable_row_length // S_vines_spacing) # Can only have an int qty of grapevines | Decimal // Decimal = an integer, type = Decimal; casted to int() for clarification 
    feasible = True

# Output
if feasible == True: # ? Can we make this feasible thing any better
    console.print(f"You have space for [green]{V_grapevine_capacity}[/green] grapevines")
    table = Table(title="Grapevine Row")
    table.add_column("Row Length")
    table.add_column("Post Length")
    table.add_column("Usable Row Length")
    table.add_column("Vine Spacing")
    table.add_column("Grapevine Capacity")
    
    table.add_row(f"{R_row_length}'", f"{E_post_length}' × 2 = {E_post_length*2}'", f"{useable_row_length}'", f"{S_vines_spacing}'", f"{V_grapevine_capacity}")
    
    console.print(table)

console.print("End of Program", style="red")