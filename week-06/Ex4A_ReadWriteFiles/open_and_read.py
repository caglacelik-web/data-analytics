# Open in read mode
f = open('about_me.txt', 'r')

# Step 1: Read full contents
print("--- Full contents ---")
print(f.read())
f.close()

# Step 2: Read 50 characters at a time
f = open('about_me.txt', 'r')
print("--- First 50 characters ---")
print(f.read(50))
print("--- Next 50 characters ---")
print(f.read(50))
f.close()

# Step 3: readline
f = open('about_me.txt', 'r')
print("--- readline(10) ---")
print(f.readline(10))
print("--- readline() ---")
print(f.readline())

for i in range(1, 5):
    print(f.readline())
f.close()

# Step 4: readlines
f = open('about_me.txt', 'r')
print("--- readlines() ---")
print(f.readlines())
f.close()

# Step 5: Combine different read methods
f = open('about_me.txt', 'r')
first_50 = f.read(50)

lines = []
for i in range(4):
    lines.append(f.readline())

next_100 = f.readlines(100)
f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")