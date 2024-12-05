# itoombes, Advent of Code
# Day 5


f1 = open("input1.txt", "r")
f2 = open("input2.txt", "r")


# Generate dictionary of pre-requisites for each page
prereqs = dict()
for rule in f1.readlines():
    prereq = rule[0:2] # Keep as string - easier to work with
    number = int(rule[3:5])
    if number not in prereqs:
        prereqs[number] = [prereq,]
    else:
        prereqs[number].append(prereq)

# For each page order
count = 0
for order in f2.readlines():
    pages = order.split(",")

    nPages = len(pages)
    outOfOrder = False
    i = 0
    # check if in order
    while (not outOfOrder) and i < nPages:
        page = int(pages[i])
        if page in prereqs:
            for prereq in prereqs[page]:
                if prereq in pages[i:-1]:
                    outOfOrder = True
        i += 1

    if not outOfOrder:
        middleIndex = (nPages - 1)//2
        count += int(pages[middleIndex])

print(count)
