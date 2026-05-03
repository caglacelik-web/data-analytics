import math

# Calculate how many boxes of tiles needed for a room
length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))

# Calculate area
room_area = length * width

# Add 10% extra for chips and breakage
tiles_needed = room_area * 1.10

# 12 tiles per box, must buy full boxes
boxes_needed = math.ceil(tiles_needed / 12)

print(f"Your room is {room_area:.0f} square feet")
print(f"With 10% extra, you need {tiles_needed:.0f} tiles")
print(f"At 12 tiles per box, you need to buy {boxes_needed} boxes")