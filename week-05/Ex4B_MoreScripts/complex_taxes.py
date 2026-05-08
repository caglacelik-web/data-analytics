# Copy pay calculation from pay_rules.py
pay_rate = float(input("What is your hourly pay rate? "))
hours_worked = float(input("How many hours did you work this week? "))
filing_status = input("What is your filing status? (single/joint) ")

# Calculate weekly gross pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = pay_rate * 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

# Calculate annual gross pay
annual_pay = gross_pay * 52

# Determine tax rate based on filing status and income
if filing_status == 'single':
    if annual_pay < 12000:
        tax_rate = 0.05
    elif annual_pay < 25000:
        tax_rate = 0.10
    elif annual_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_pay < 12000:
        tax_rate = 0.00
    elif annual_pay < 25000:
        tax_rate = 0.06
    elif annual_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate tax and net pay
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# Print results
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withheld:.2f}")
print(f"Your net pay is ${net_pay:.2f}")
    