# itoombes, Advent of Code 2024
# Day 24

import copy

TEST = 1
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
    return (x + y) & (2 ** nBits - 1)

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

def main():
    values = parse_init_values()
    expected = parse_expected_out(values)
    predicates = parse_predicates()
    # Generate all pairs of predicates
    pairs = list()
    for i in range(0, len(predicates) - 1):
        for j in range(i + 1, len(predicates)):
            pairs.append((i, j))
    # Generate all groups of four pairs
    swapgroups = list()
    for i in range(0, len(pairs) - 3):
        for j in range(i + 1, len(pairs) - 2):
            for k in range(j + 1, len(pairs) - 1):
                for l in range(k + 1, len(pairs)):
                    swapgroups.append((i, j, k, l))
    #print(swapgroups)
    # Go thru every group of four
    while len(swapgroups) > 0:
        predVar = copy.deepcopy(predicates)
        valVar = copy.deepcopy(values)
        swaps = swapgroups.pop(0)
        for ip in swaps:
            in11, in12, gate1, out1 = predVar[pairs[ip][0]]
            in21, in22, gate2, out2 = predVar[pairs[ip][1]]
            predVar[pairs[ip][0]] = (in11, in12, gate1, out2)
            predVar[pairs[ip][1]] = (in21, in22, gate2, out1)
        outValues = apply_predicates(valVar, predVar)
        out = 0
        for k in outValues.keys():
            if k[0] == "z":
                out = out | (outValues[k] << int(k[1:]))
        if out == expected:
            print(swaps)

    

if __name__ == "__main__":
    main()
