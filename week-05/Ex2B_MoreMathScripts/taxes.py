# Calculate federal tax withheld from monthly salary
salary = float(input("What is your monthly salary? "))

# Federal tax rate is 23%
tax_rate = 0.23

# Calculate tax withheld
tax_withheld = salary * tax_rate
take_home = salary - tax_withheld

print(f"Your monthly salary is ${salary:.2f}")
print(f"Federal taxes withheld (23%): ${tax_withheld:.2f}")
print(f"Your take home pay is ${take_home:.2f}")