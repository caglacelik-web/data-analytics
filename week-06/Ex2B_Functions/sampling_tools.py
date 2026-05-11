import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# a) Product of the Day - randomly select one item
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# b) Usability survey - select 3 items without replacement
survey_products = random.sample(products, 3)
print(f"\nProducts selected for usability survey: {survey_products}")

# c) Randomized order for presentation
random.shuffle(products)
print(f"\nProducts in randomized order: {products}")

# d) Simulated daily transaction count
transaction_count = random.randint(50, 300)
print(f"\nSimulated daily transaction count: {transaction_count}")