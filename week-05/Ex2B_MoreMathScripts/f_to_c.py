# Convert Fahrenheit to Celsius
# Formula: (F - 32) * 5/9

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"The temperature {fahrenheit:.1f}°F is equal to {celsius:.1f}°C")