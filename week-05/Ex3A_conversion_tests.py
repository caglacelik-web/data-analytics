# Description: This script tests various numeric conversion techniques
# Author: Cagla Celik

# Define variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Print each variable and its type
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Casting as integer using int()
# int(a)  # Error. Can't convert a string with spaces and decimals directly
# int(b)  # This works. b is '55' which is a clean number string
print(int(b))
# int(c)  # Error. Contains letters
# int(d)  # Error. contains letters

# Casting as float using float()
print(float(a))  # works! strips spaces and converts
print(float(b))  # works! converts to 55.0
# float(c)  # Error. contains letters
# float(d)  # Error. contains letters

# Cast a as float then integer
print(int(float(a)))  # works! first converts to 101.1 then drops decimal to get 101

# Strip spaces from a and d
print(a.strip())
print(d.strip())

# Use slicing to get just the numeric portion
# c = "402 Stevens" - numbers are at index 0,1,2
c_num = int(c[0:3])
print(c_num, type(c_num))

# d = 'Number 5 ' - the number 5 is at index 7
d_num = int(d[7])
print(d_num, type(d_num))