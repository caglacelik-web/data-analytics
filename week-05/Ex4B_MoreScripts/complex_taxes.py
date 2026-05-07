pay_rate = 15
hours_worked = 40
filing_status = "single"

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)

else:
    gross_pay = hours_worked * pay_rate

    annual_income = gross_pay * 52
    