# ValueError
try:
    x = int('hello')
except ValueError:
    print("ValueError: Cannot convert 'hello' to an integer")
else:
    print(x)
finally:
    print("Let's try another one...\n")

# NameError
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to use an undefined variable")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# TypeError
try:
    result = 'hello' + 5
except TypeError:
    print("TypeError: Cannot add a string and an integer together")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# SyntaxError - has to be caught differently since it happens before code runs
try:
    eval('x === 5')
except SyntaxError:
    print("SyntaxError: Invalid syntax detected")
else:
    print("No error")
finally:
    print("Let's try another one...\n")