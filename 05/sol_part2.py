# itoombes, Advent of Code
# Day 5


f1 = open("input1.txt", "r")
f2 = open("input2.txt", "r")

import math

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

    if outOfOrder:
        # Want to re-sort these out-of-order lists
        # Assuming all of them CAN be correctly ordered
        i = 0
        print(nPages)
        while i < nPages:
            swapped = False
            if int(pages[i]) in prereqs:
                # Go thru each prereq - if match found, swap last pre-req and value
                for prereq in prereqs[int(pages[i])]:
                    j = nPages - 1
                    while j > i and swapped == False:
                        if pages[j] == prereq:
                            print(pages)
                            print(f"Page error {pages[j]} | {pages[j]}")
                            swapped = True
                            swp = pages[i]
                            pages[i] = pages[j]
                            pages[j] = swp
                            print(f"Post-swap : {pages}")
                            break
                        j -= 1
            if not swapped:
                i += 1
            else:
                i = 0
        print(pages)
        increment = int(pages[math.floor((nPages - 1)/2)])
        print(increment)
        count += increment 

print(count)
