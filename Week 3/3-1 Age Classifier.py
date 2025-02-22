"""
## Program 3-3 Age Classifier
**Prof's Notes**: *Standard IF problem with lots of traps for unwary students that have nothing to do with the IF statement!!!*

**Problem** (pg197)
Write a program that asks the user to enter a person's age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. Following are the guidelines:

- If the person is 1 year old or less, they are an infant.
- If the person is older than 1 year, but younger than 13 years, they are a child.
- If the person is at least 13 years old, but less than 20 years old, they are a teenager.
- If the person is at least 20 years old, they are an adult.
"""
# Age Classifier V1, Program 3-3 Textbook, Mon, Feb 10, 2025 6 PM
# Classifies a given age by preset ranges
#
# Input
#   Age from user
#
# Output
#   Age Classification

# Libraries
import pyinputplus as pyip # Input validation

# Globals
# Sets the age ranges for their give classifications, MUST NOT overlap (stops are exclusive, doesn't count)
# range(start, stop) start is inclusive, stop is not; (0,2) includes 0, 1 but stops before 2
infant_range = range(0,2) 
child_range = range(2,13)
teenager_range = range(13,20)
adult_age = 20

# Program
print(f"This program classifies you based on your age")

# User Input
age = pyip.inputInt("Please enter your age: ", min=0) # minimum = 0; If you age is less than 0 you're not born or uh.. a time traveler?

# Calculates Age Range
if age < adult_age:
    if age in teenager_range:
        classification = "Teenager"
    elif age in child_range:
        classification = "Child"
    else:
        classification = "Infant"
else:
    classification = "Adult"

# Output
print(f"You are {age} year(s) old, you are an {classification}")

print("End of Program")