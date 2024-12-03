# itoombes, Advent of Code 2024
# Day 3

import re

# Extract all multiplication instructions
f = open("input.txt", "r")
instructions= re.findall("mul\(\d*,\d*\)|do\(\)|don't\(\)", f.read())
print(instructions)

# Read thru the instructions
total = 0
enabled = True 
for instruction in instructions:
    print(instruction)
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif enabled:
        # Extract the values
        values = instruction.split(",")
        x = int(values[0][4:])
        y = int(values[1][:-1])
        #print(f"{x}, {y}")
        # Add to the total
        total += x * y
        #print(f"\t{total}")
    print(total)
