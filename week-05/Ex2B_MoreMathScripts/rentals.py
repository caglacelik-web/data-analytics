import math

# Calculate van rentals for a tour group
num_tourists = int(input("How many tourists are going on the tour? "))

# Van details
van_capacity = 15
van_cost_per_day = 250

# Calculate vans needed - must round up to fit everyone
vans_needed = math.ceil(num_tourists / van_capacity)

# Calculate costs
total_cost = vans_needed * van_cost_per_day
cost_per_person = total_cost / num_tourists

print(f"Number of tourists: {num_tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# Note: leftover money exists because we charged per person but paid for
# full vans. 3 vans hold 45 people but only 38 are going, so 7 seats
# are empty but still paid for collectively.