# Rule of 72 - how long to double your savings
current_savings = 10000
interest_rate = 0.06

# Rule of 72 formula: divide 72 by the interest rate percentage
years_to_double = 72 / (interest_rate * 100)
doubled_balance = current_savings * 2

# Display results
print("Your current savings is " + str(current_savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth " 
      + format(doubled_balance, ".2f") + " in " + format(years_to_double, ".1f") + " years")