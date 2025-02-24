# Hot Dog Cookout Calculator V1, Exam 1, Problem 1, Sun, Feb 23, 2025 6PM
# Calculates the number of packages of hot dogs and packages of hot dog buns needed for a cookout
#
# Input
#   • number of people attending the cookout 
#   • number of hot dogs each person will be given 
#   • number of hot dogs per hot dog package 
#   • number of hot dog buns per package of buns
#
# Output
#   • size of hot dog package (PassIn)
#   • size of hot dog bun package (PassIn)
#   • minimum number of packages of hot dogs required 
#   • minimum number of packages of hot dog buns required  
#   • number of hot dogs that will be left over 
#   • number of hot dog buns that will be left over

# Libraries
import pyinputplus as pyip # Input Validation
from math import ceil # If this was a bigger program I'd import the whole library
from rich.console import Console # Fancy Output
from rich.table import Table # Fancy Output

# Program
console = Console()
console.print(f"This program calculates how many packages of hot dogs and buns you will need for a cookout with minimal leftovers.", style="green")

# User Input
attendance_count: int = pyip.inputInt("How many people will attend your cookout? ", min=1)
hotdogs_per_person: int = pyip.inputInt("How many hot dogs will each person receive? ", min=1)
hotdogs_per_package: int = pyip.inputInt("How many hot dogs does a package contain? ", min=1)
buns_per_package: int = pyip.inputInt("How many buns does a package contain? ", min=1)

# Calculates: (Required: hot dogs, hot dog packages, and bun packages) & (Leftover: hot dogs and buns)
hotdogs_required: int = attendance_count * hotdogs_per_person

hotdog_packages_required: int = ceil(hotdogs_required / hotdogs_per_package)
bun_packages_required: int = ceil(hotdogs_required / buns_per_package)
hotdog_leftovers: int = ( hotdogs_per_package * hotdog_packages_required ) - hotdogs_required
bun_leftovers: int = ( buns_per_package * bun_packages_required ) - hotdogs_required

# Output
print(f"\n{attendance_count} guest(s) each having {hotdogs_per_person} hot dog(s) will require {hotdogs_required} hot dog(s)\n")
table = Table()
table.add_column("")
table.add_column("Pkg Size")
table.add_column("Min Pkg Qty")
table.add_column("Leftovers")

table.add_row("Hot Dogs", f"{hotdogs_per_package}", f"{hotdog_packages_required}", f"{hotdog_leftovers}")
table.add_row("Buns", f"{buns_per_package}", f"{bun_packages_required}", f"{bun_leftovers}")

console.print(table)

console.print("End of Program", style="red")