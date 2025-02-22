# Expressions V1, Mon Jan 27, 2025 6 PM
# Calculates various mathematical expressions, Duplicated to show ambiguous vs unambiguous coding
# 
# Input
#   No user input
# 
# Output
#   Answers to pre-defined expressions

# Original Expressions for reference: Some changes in initial versions of expression due to syntax errors
# 1 a = 6 + 3 * 5
# 2 a = 12 / 2 – 4
# 3 a = 9 + 14 * 2 – 6
# 4 a = 6 / 2(1+2)
# 5 a = (6 + 2) * 3
# 6 a = 14 / (11 – 4)
# 7 a = 9 + 12 * (8 - 3)
# 8 a = 6 / 2(1+2)

print("This program calculates various pre-defined mathematical expressions.")
# 1
a = 6 + 3 * 5
print("1.", a)
a = 6 + (3 * 5) # Added Parentheses
print("1.", a)

# 2
a = 12 / 2 - 4 # replaced "–" (U+2013) to -
print("2.", a)
a = (12 / 2) - 4 # Added Parentheses
print("2.", a)

# 3
a = 9 + 14 * 2 - 6 # replaced "–" (U+2013) to -
print("3.", a)
# 3
a = 9 + (14 * 2) - 6 # Added Parentheses
print("3.", a)

# 4
a = 6 / 2 * (1+2) # Added * between 2 & (
print("4.", a)
a = (6 / 2) * (1+2) # Added Parentheses
print("4.", a)

# 5
a = (6 + 2) * 3
print("5.", a)
a = (6 + 2) * 3
print("5.", a)

# 6
a = 14 / (11 - 4) # replaced to -
print("6.", a)
a = 14 / (11 - 4)
print("6.", a)

# 7
a = 9 + 12 * (8 - 3)
print("7.", a)
a = 9 + (12 * (8 - 3)) # Added 2x Parentheses
print("7.", a)

# 8
a = 6 / 2 * (1+2) # Added * between 2 & (
print("8.", a)
a = (6 / 2) * (1+2) # Added Parentheses
print("8.", a)

print("End of Program.")