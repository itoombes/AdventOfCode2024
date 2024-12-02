# itoombes, Advent of Code 2024
# Day 2


safeCount = 0


f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    numbers = line.split(' ')

    decreasing = False

    i = 1
    count = len(numbers)
    safe = True

    while (i < count) and safe:
        diff = int(numbers[i - 1]) - int(numbers[i])
        
        # Ensure in range
        if (diff == 0) or (diff < -2) or (diff > 2):
            safe = False

        # Ensure consistency
        if diff < 0:
            if (i == 1):
                decreasing = True
            elif decreasing:
                diff *= -1
            safe = False
        if (diff > 0) and (i != 1) and decreasing:
            safe = False
        
        # If here, then so far valid
        i += 1

    if safe:
        safeCount += 1
        print(f"{line} is safe! | Count is {safeCount}")
    else:
        print(f"{line} is not safe")
