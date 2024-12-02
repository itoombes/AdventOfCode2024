# itoombes, Advent of Code 2024
# Day 2

import copy

safeCount = 0


f = open("input.txt", "r")
lines = f.readlines()


def checkSafety(numbers, depth):
    count = len(numbers)
    i = 1
    
    decreasing = False
    numRemoved = False
    while (i < count):
        diff = int(numbers[i - 1]) - int(numbers[i])

        if (diff == 0) or (diff < -3) or (diff > 3):
            if depth == 1:
                return False
            attempt1list = copy.deepcopy(numbers)
            attempt1list.pop(i - 1)
            attempt2list = copy.deepcopy(numbers)
            attempt2list.pop(i)
            print("\t One number invalid - try with removals")
            print(f"\t{attempt1list}")
            print(f"\t{attempt2list}")
            if checkSafety(attempt1list, 1) or checkSafety(attempt2list, 1):
                return True
            else:
                return False


        if (i == 1):
            if diff < 0:
                decreasing = True
        elif diff < 0 and not decreasing:
            if depth == 1:
                return False
            attempt1list = copy.deepcopy(numbers)
            attempt1list.pop(i - 1)
            attempt2list = copy.deepcopy(numbers)
            attempt2list.pop(i)
            print("\t One number invalid - try with removals")
            print(f"\t{attempt1list}")
            print(f"\t{attempt2list}")
            if checkSafety(attempt1list, 1) or checkSafety(attempt2list, 1):
                return True
            else:
                return False
        elif diff > 0 and decreasing:
            if depth == 1:
                return False
            attempt1list = copy.deepcopy(numbers)
            attempt1list.pop(i - 1)
            attempt2list = copy.deepcopy(numbers)
            attempt2list.pop(i)
            print("\t One number invalid - try with removals")
            print(f"\t{attempt1list}")
            print(f"\t{attempt2list}")
            if checkSafety(attempt1list, 1) or checkSafety(attempt2list, 1):
                return True
            else:
                return False
        i += 1
    
    return True




for line in lines:
    numbers = line.split(' ')
    print(f"Processing {numbers}")
    if checkSafety(numbers, 0):
        safeCount += 1
        print(f"\t Safe : count now {safeCount}")
    else:
        print("\t Not Safe")

print(safeCount)
