#making the variables comments
#so i can run the code with different values

#pay_rate = 17.30       
#hours_worked = 45
#pay_rate = 12.50
#hours_worked = 20
pay_rate = 18.75
hours_worked = 40


if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours_worked * pay_rate
print(f"Total pay for the week: ${total_pay:.2f}")