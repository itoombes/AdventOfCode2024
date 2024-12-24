# itoombes, Advent of Code 2024
# Day 24

import copy

TEST = 0
if TEST:
    VALUES = "test3.txt"
    PREDICATES = "test4.txt"
else:
    VALUES = "input1.txt"
    PREDICATES = "input2.txt"

def parse_init_values():
    f = open(VALUES, "r")
    values = dict()
    for line in f.readlines():
        values[line[0:3]] = int(line[-2:-1])
    return values

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

def parse_predicates():
    f = open(PREDICATES, "r")
    predicates = list()
    for line in f.readlines():
        line = line.replace("\n", "")
        in1, gate, in2, _, out = line.split(" ")
        predicates.append((in1, in2, gate, out))
    return predicates

def apply_predicates(values, predicates):
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
    return values

def extract_z_values(values):
    expected = parse_expected_out(values)
    nZ = len(bin(expected)) - 3 + 100 # Want two digit with leading zeros
    for i, b in enumerate(bin(expected)[2:]):
        zed = "z" + str(nZ - i)[1:]
        values[zed] = b
    return values

def main():
    values = parse_init_values()
    expected = parse_expected_out(values)
    print(bin(expected))
    print(extract_z_values(values))
    

if __name__ == "__main__":
    main()
