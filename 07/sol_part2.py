# itoombes, Advent of Code 2025
# Day 7

def parse_input():
    if False:
        f = open("dummyInput.txt", "r")
    else:
        f = open("input.txt", "r")
    equations = list()
    for line in f.readlines():
        line = line.split(":")
        result = int(line[0])
        values = line[1][1:].split(" ")
        for i in range(0, len(values)):
            values[i] = int(values[i])
        equations.append((result, values))
    return equations 

def is_possible(equation):
    print(f"Validate {equation}")
    # Iterate thru each possible operation comparison
    ops = [0] * (len(equation[1]) - 1)
    while True:
        currentTotal = equation[1][0]
        # Go through variant
        for i in range(1, len(equation[1])):
            if ops[i - 1] == 1:
                currentTotal += equation[1][i]
            else if ops[i - 1] == 2:
                currentTotal = int(str(currentTotal) + str(equation[1][i]))
            else:
                currentTotal *= equation[1][i]
            # Skip results when already over total
            if currentTotal > equation[0]:
                break
            if currentTotal == equation[0] and i == len(equation[1]) - 1:
                print(f"\tValid : {ops}")
                return True
            print(f"\tInvalid : {currentTotal}")

        # Iterate to next variant
        i = 0
        while True: 
            if ops[i] == 0:
                ops[i] = 1
                for j in range(0, i):
                    ops[j] = 0
                break
            i += 1
            # If here, have no values that will match 
            if i == len(ops):
                print("\tNo valid values")
                return False


def main():
    equations = parse_input()
    count = 0
    for equation in equations:
        if is_possible(equation):
            count += equation[0]
            print(f"\t{count}")
    print(count)

if __name__ == "__main__":
    main()
