# itoombes, Advent of Code 2024
# Day 2


safeCount = 0


f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    numbers = line.split(' ')
    print(f"Processing {numbers}")

    decreasing = False

    i = 1
    count = len(numbers)
    safe = True
    while (i < count) and safe:
        diff = int(numbers[i - 1]) - int(numbers[i])
        
        if (diff == 0) or (diff < -3) or (diff > 3):
            print("\tDifference out of range : not safe")
            safe = False

        if (i == 1):
            if diff < 0:
                decreasing = True
        elif ((diff < 0) and not decreasing) or ((diff > 0) and decreasing):
            print("\tGradient inconsistent : not safe")
            safe = False
        
        i += 1

    if safe:
        safeCount += 1
        print(f"\t Safe! Current count is {safeCount}")

    print(safeCount)
