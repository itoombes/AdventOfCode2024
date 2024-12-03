# itoombes, Advent of Code 2024
# Day 3

import re

# Extract all multiplication instructions
f = open("input.txt", "r")
muls = re.findall("mul\(\d*,\d*\)", f.read())
print(muls)

# Read thru the instructions
total = 0
for mul in muls:
    # Extract the values
    values = mul.split(",")
    x = int(values[0][4:])
    y = int(values[1][:-1])
    print(f"{x}, {y}")
    # Add to the total
    total += x * y
    print(f"\t{total}")
