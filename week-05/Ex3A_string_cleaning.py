# String cleaning exercises
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert all names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert all names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove $ from salaries
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))
print(type(salary_1.replace("$", "")))

# Chain replace() and int() to get a usable integer from salary_1
# First remove $ and comma, then convert to int
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int, type(salary_1_int))