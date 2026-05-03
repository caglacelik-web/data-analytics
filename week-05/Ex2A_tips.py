# Calculate tip amount on a restaurant bill
bill_amount = float(input("What is your restaurant bill amount? "))
tip_percentage = float(input("What tip percentage would you like to leave? (enter as decimal e.g. 0.20) "))

# Calculate tip
tip_amount = bill_amount * tip_percentage

# Display results
print(f"The tip on a ${bill_amount:.2f} restaurant bill is ${tip_amount:.2f}")

# Possible pitfalls with input():
# 1. If the user types letters instead of numbers, the program will crash
# 2. If the user types a percentage like "20" instead of "0.20" the result will be wrong
# 3. input() always returns a string, so you must convert it with float() or int() for math operations. If you forget to convert, you'll get a TypeError when trying to multiply a string by a float.
