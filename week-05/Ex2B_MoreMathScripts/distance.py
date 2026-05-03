import math

# Calculate distance between two coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance formula: square root of (x2-x1)^2 + (y2-y1)^2
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")