# itoombes, Advent of Code
# Day 5


f1 = open("input1.txt", "r")
f2 = open("input2.txt", "r")

import heapq

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
        #print(pages)
        # Generate adjacencies
        adjacency = dict()
        for page in pages:
            adjacency[page] = list()
        # Go thru each page and establish how many pages are adjacent
        for page in pages:
            if int(page) in prereqs:
                for prereq in prereqs[int(page)]:
                    if prereq in pages:
                        adjacency[prereq].append(page)
        #print(f"\t{adjacency}")
        # Generate p-queue
        order = list()
        for page in pages:
            heapq.heappush(order, (len(adjacency[page]), page))
        
        # Sort the list
        sortedPages = list()
        i = 0
        while i < nPages:
            sortedPages.append(heapq.heappop(order)[1])
            i += 1

        sortedPages.reverse()

        print(f"{pages}")
        print(f"\t{adjacency}")
        print(f"{sortedPages}")
        mid = (nPages - 1) // 2
        print(f"\t{sortedPages[mid]}")
        count += int(sortedPages[mid])
        print(f"\t{count}")
        i = 0
        while i < nPages:
            page = int(sortedPages[i])
            if page in prereqs:
                for prereq in prereqs[page]:
                    if prereq in sortedPages[i:-1]:
                        print("INCORRECT SORT!")
                        print(f"{prereqs[int(sortedPages[i])]}|{sortedPages[i]})")
                        ValueError()
            i += 1


print(count)
