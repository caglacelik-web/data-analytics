current_bank_balance = 1600
savings_goal = 2000
weekly_savings = 100

while current_bank_balance < savings_goal:

        current_bank_balance = current_bank_balance + weekly_savings

        print(f"This week my balance increased to ${current_bank_balance}")
        if current_bank_balance >= savings_goal /2:
            print("Almost there! This week my balance is up to " + str(current_bank_balance) + " dollars, which is more than half of my savings goal!")
        if current_bank_balance >= savings_goal * 0.75: 
            current_bank_balance = current_bank_balance - 25
            print("So close! After treating myself, this week my balance is up to " + str(current_bank_balance) + " dollars, which is more than 75% of my savings goal!")
print(f"Goal met! My current balance is ${current_bank_balance}")