# itoombes, Advent of Code 2024
# Day 24

import copy
from sys import argv

PREDICATES = "input2.txt"

def parse_init_values(x, y):
    values = dict()
    nBits = 45
    for i in range(0, nBits):
        index = i + 100
        xKey = "x" + str(index)[1:]
        yKey = "y" + str(index)[1:]
        values[xKey] = x & (1 << i)
        values[yKey] = y & (1 << i)
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
    print(f"x : {x}, y : {y}")
    return x + y

def extract_z_values(values):
    zValues = dict()
    expected = parse_expected_out(values)
    nZ = len(bin(expected)) - 3 + 100 # Want two digit with leading zeros
    for i, b in enumerate(bin(expected)[2:]):
        zed = "z" + str(nZ - i)[1:]
        zValues[zed] = b
    return zValues

def check_valid(values, predicates, expected, zValues):
    initValues = copy.deepcopy(values)
    initPredicates = copy.deepcopy(predicates)
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
    out = 0
    for k in values.keys():
        if k[0] == "z":
            out = out | (values[k] << int(k[1:]))
    print(bin(out))
    print(bin(expected))
    for k in zValues.keys():
        if k[0] == "z" and int(zValues[k]) != int(values[k]):
            print(f"{values[k]}, {zValues[k]}")
            failZ.append(k)
    notablePredicates = list()
    for i, p in enumerate(initPredicates):
        in1, in2, gate, out = p
        if gate == "AND":
            gate = "&"
        elif gate == "OR":
            gate = "|"
        elif gate == "XOR":
            gate = "^"
        string = f"{str(i + 1001)[1:]}: {in1} {gate} {in2} -> {out}"
        string += f" | {values[in1]} {gate} {values[in2]} -> {values[out]}"
        if out in failZ:
            string = "\033[0;31m" + string + "\033[0m"
            notablePredicates.append(string)
        elif out[0] == "z":
            string = "\033[0;32m" + string + "\033[0m"
            #notablePredicates.append(string)
        print(string)
    print()
    for s in notablePredicates:
        print(s)
    print(f"# Incorrect : {len(failZ)}")
    return len(failZ)

def main():
    # Extract data from files
    predicates = parse_predicates()

    # Confirm valid for (0, 0), (0, 1), (1, 0), (1, 1)
    while True
    values = parse_init_values(0, 0)
    zValues = extract_z_values(values)
    expected = parse_expected_out(values) 
    check_valid(values, predicates, expected, zValues)

if __name__ == "__main__":
    main()
