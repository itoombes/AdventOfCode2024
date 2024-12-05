# itoombes, Advent of Code
# Day 5

f1 = open("input1.txt", "r")
f2 = open("input2.txt", "r")


# Generate dictionary of pre-requisites for each page
prereqs = dict()
for rule in f1.readlines():
    prereq = int(rule[0:2])
    number = int(rule[3:5])
    if number not in prereqs:
        prereqs[number] = [prereq,]
    else:
        prereqs[number].append(prereq)

