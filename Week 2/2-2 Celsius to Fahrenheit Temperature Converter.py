# Celsius to Fahrenheit Temperature Converter V1, Program 2-9 Textbook, Sun Feb 2, 2025 6 PM
# Converts Celsius given by user to Fahrenheit
# 
# Input
#   Celsius - User Input (Not specified in requirements)
# 
# Output
#   Fahrenheit - Rounded to one decimal place (standard)
#
# Conversion Formula 𝐹 = (9/5)𝐶 + 32

# Libraries
import pyinputplus as pyip # Used for data validation

# Program
print("This program converts Celsius to Fahrenheit")

# User input
celsius = pyip.inputNum("Enter a temperature in Celsius (°C): ") 

# Calculation
fahrenheit = ((9/5) * celsius) + 32

# Output
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
print("End of Program.")