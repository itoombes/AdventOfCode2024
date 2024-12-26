# itoombes, Advent of Code 2024
# Day 24

import copy

VALUES = "input1.txt"
PREDICATES = "input2.txt"

def parse_init_values():
    f = open(VALUES, "r")
    values = dict()
    for line in f.readlines():
        values[line[0:3]] = int(line[-2:-1])
    return values

def parse_predicates():
    f = open(PREDICATES, "r")
    predicates = list()
    for line in f.readlines():
        line = line.replace("\n", "")
        in1, gate, in2, _, out = line.split(" ")
        predicates.append((in1, in2, gate, out))
    return predicates

def parse_expected_out(values):
    x = 0
    y = 0
    nBits = 0
    for k in values.keys():
        if k[0] == "x":
            x |= (values[k] << int(k[1:]))
            if (int(k[1:])) + 1 > nBits:
                nBits = int(k[1:]) + 1
        elif k[0] == "y":
            y |= (values[k] << int(k[1:]))
    return x + y

def extract_z_values(values):
    zValues = dict()
    expected = parse_expected_out(values)
    nZ = len(bin(expected)) - 3 + 100 # Want two digit with leading zeros
    for i, b in enumerate(bin(expected)[2:]):
        zed = "z" + str(nZ - i)[1:]
        zValues[zed] = b
    return zValues

def check_valid(values, predicates):
    expected = extract_z_values(values)
    predicates = copy.deepcopy(predicates) 
    while len(predicates) > 0:
        in1, in2, gate, out = predicates.pop(0)
        if in1 not in values.keys() or in2 not in values.keys():
            predicates.append((in1, in2, gate, out))
            continue
        if gate == "AND":
            values[out] = values[in1] & values[in2]
        elif gate == "XOR":
            values[out] = values[in1] ^ values[in2]
        elif gate == "OR":
            values[out] = values[in1] | values[in2]
    failZ = list()
    for z in expected.keys():
        if int(values[z]) != int(expected[z]):
            failZ.append(f"{z} = {values[z]}")
    return failZ

def main():
    # Extract data from files
    initPredicates = parse_predicates()
    values = parse_init_values()
    # Set default values
    for i in range(0, 45):
        keyIndex = str(i + 100)
        xKey = "x" + keyIndex[1:]
        yKey = "y" + keyIndex[1:]
        values[xKey] = 0
        values[yKey] = 0
    initValues = copy.deepcopy(values)
    # Iterate over adder, make sure that it works
    # Iterate over 
    # Test low
    for x, y in ((0, 0), (1, 0), (1, 1)):
        values = copy.deepcopy(initValues)
        values["x00"] = x
        values["y00"] = y
        failed = check_valid(values, initPredicates)
        if len(failed) > 0:
            print("x00, y00 combinations failed")
            exit()
    for i in range(1, 45):
        # Tests adding and carrying
        for xH, xL, yH, yL in ((1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 1, 1, 0), (1, 1, 1, 1)):
            values = copy.deepcopy(initValues)
            key = i + 100 
            xHigh = "x" + str(key)[1:]
            yHigh = "y" + str(key)[1:]
            xLow = "x" + str(key - 1)[1:]
            yLow = "y" + str(key - 1)[1:]
            values[xHigh] = xH
            values[xLow] = xL
            values[yHigh] = yH
            values[yLow] = yL
            progress = ""
            if xH: progress += xHigh + " "
            if xL: progress += xLow + " "
            if yH: progress += yHigh + " "
            if yL: progress += yLow + " "
            print(progress)
    # i = 45
        

    expected = parse_expected_out(values) 
    zValues = extract_z_values(values)


if __name__ == "__main__":
    main()
