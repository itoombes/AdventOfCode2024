# itoombes, Advent Of Code 2024
# Day 1, Part 1


# Extract the input data (input.txt) into two lists
left = list()
right = list()

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    left.append(int(line[:5]))
    right.append(int(line[8:13]))

# Sort the lists
left.sort()
right.sort()

# Sum the minimum on both lists
n_items = len(left)
assert(n_items == len(right))
print(f"Number of items per list: {len(left)}")

i = 0
distance = 0
while i < n_items: 
    diff = left[i] - right[i]
    if diff < 0:
        diff *= -1
    distance += diff
    print(f"Element {i} : Left {left[i]} : Right {right[i]} : Diff {diff} : Current Distance {distance}")
    i += 1


print(distance)
