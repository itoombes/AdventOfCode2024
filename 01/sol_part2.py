# itoombes, Advent Of Code 2024
# Day 1, Part 2


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

print(left)
print(right)


# Iterate thru the lists
score = 0

rightCount = len(right)
rightIndex = 0

score = 0
for leftIndex, leftElement in enumerate(left):
    print(f"Evaluating left element {leftElement}")
    count = 0
    while True:
        if rightIndex == rightCount:
            print("Out of elements in right list")
            print(score)
            quit()
        print(f"\t{right[rightIndex]}")
        if leftElement > right[rightIndex]:
            pass
        elif leftElement == right[rightIndex]:
            print("\t\tMatch!")
            count += 1
        else:
            break
        rightIndex += 1
    score += leftElement * count 
    print(f"Element : {leftElement} | Matches : {count} | Current Score : {score}")

print(score)
quit()

rightCount = len(right)

rightIndex = 0
for leftIndex, leftElement in enumerate(left):
    # Iterate thru any elements that are lower than the list on the left
    while leftElement < right[rightIndex]:
        rightIndex += 1
        if rightIndex == rightCount:
            print(f"Ran out of right elements with left element {leftElement}")
            print(score) # No more elements in right list
            quit()
    # Count the number of elements that are the same
    count = 0
    while leftElement == right[rightIndex]:
        count += 1
        rightIndex += 1
        if rightIndex == rightCount:
            score += count * leftElement
            print(score)
            quit()
    # If here, right elements now larger than left element
    # Add and iterate to next left element
    score += count * leftElement


print(score)
