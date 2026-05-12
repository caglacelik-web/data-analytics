def display_mailing_label(name, address, city, state, zip):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip}")

def add_numbers(*args):
    result = sum(args)
    equation = ' + '.join(str(n) for n in args)
    print(f"{equation} = {result}")

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")
    print()

# Test display_mailing_label
display_mailing_label('Cagla Celik', '123 Main St', 'Chicago', 'IL', '60601')
display_mailing_label('John Doe', '456 Oak Ave', 'New York', 'NY', '10001')

# Test add_numbers
add_numbers(5)
add_numbers(3, 7)
add_numbers(1, 2, 3, 4, 5)

# Test display_receipt
display_receipt(50.00, 60.00)   # overpay
display_receipt(50.00, 50.00)   # exact
display_receipt(50.00, 30.00)   # underpay