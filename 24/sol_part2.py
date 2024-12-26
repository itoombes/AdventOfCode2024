# itoombes, Advent of Code 2024
# Day 24

import copy

TEST = 0
if TEST:
    VALUES = "test3.txt"
    PREDICATES = "test4.txt"
else:
    VALUES = "input1.txt"
    PREDICATES = "manualinput.txt"

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

def extract_base_predicates(values, predicates):
    for i, p in enumerate(predicates):
        in1, in2, gate, out = p
        if in1 in values.keys() and in2 in values.keys():
            if gate == "AND":
                out = values[in1] & values[in2]
            elif gate == "OR":
                out = values[in1] | values[in2]
            elif gate == "XOR":
                out = values[in1] ^ values[in2]
            print(f"{i + 1} : {out}")

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
        if in1 in failZ or in2 in failZ or out in failZ:
            string = "\033[0;31m" + string + "\033[0m"
            notablePredicates.append(string)
        elif in1[0] == "z" or in2[0] == "z" or out[0] == "z":
            string = "\033[0;32m" + string + "\033[0m"
            notablePredicates.append(string)
        print(string)
    print()
    for s in notablePredicates:
        print(s)
    print(f"# Incorrect : {len(failZ)}")

def main():
    # Extract data from files
    setValues = parse_init_values()
    zValues = extract_z_values(setValues)
    expected = parse_expected_out(setValues) 
    setPredicates = parse_predicates()
    extract_base_predicates(setValues, setPredicates)
    while True:
        values = copy.deepcopy(setValues)
        predicates = copy.deepcopy(setPredicates)
        print("Input wires to swap:")
        swapMem = list()
        for i in range(1, 5):
            while True:
                try:
                    userInput = input()
                    swap1, swap2 = userInput.split(" ")
                    # Exit early
                    swap1 = int(swap1) - 1 # Using LINE NUMBER, not index
                    swap2 = int(swap2) - 1
                    in11, in12, gate1, out1 = predicates[swap1]
                    in21, in22, gate2, out2 = predicates[swap2]
                    predicates[swap1] = (in11, in12, gate1, out2)
                    predicates[swap2] = (in21, in22, gate2, out1)
                    print(f"Swap {i} successful!")
                    swapMem.append((swap1, swap2))
                except:
                    if userInput == "q" or userInput == "Q":
                        exit()
                    print("Illegal swap attempt! Try again.")
                    continue
                break
        if check_valid(values, predicates, expected, zValues):
            print("Valid!")
            for swap in swapMem:
                print(f"{swap[0]}, {swap[1]}")
            exit()

if __name__ == "__main__":
    main()
