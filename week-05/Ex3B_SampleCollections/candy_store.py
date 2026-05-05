# Candy store combinations using tuples and sets

# Tuple of candy types
candy_types = ("Skittles", "Starburst", "Jolly Ranchers")

# Tuple of fruity flavors
flavors = ("strawberry", "watermelon", "mango", "peach")

# Create a set of candy combinations
candy_combos = set()
candy_combos.add(candy_types[0] + " " + flavors[1])  # Skittles watermelon
candy_combos.add(candy_types[1] + " " + flavors[0])  # Starburst strawberry
candy_combos.add(candy_types[2] + " " + flavors[2])  # Jolly Ranchers mango
candy_combos.add(candy_types[0] + " " + flavors[3])  # Skittles peach

# Print the candy options
print("Today's candy options include:")
print(candy_combos)
print("Today's candy options include:")
print(candy_combos)
print("Today's candy options include:")
print(candy_combos)