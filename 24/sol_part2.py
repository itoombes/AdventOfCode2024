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

def sort_predicates(values, predicates):
    variablePredicates = list()
    setCache = dict()
    keys = values.keys()
    outputs = list()
    for i, p in enumerate(predicates):
        in1, in2, gate, out = p
        # Collect outputs
        outputs.append(out)
        # Cache preprepared results
        if in1 in keys and in2 in keys:
            if gate == "AND":
                setCache[i] = values[in1] & values[in2]
            elif gate == "OR":
                setCache[i] = values[in1] | values[in2]
            elif gate == "XOR":
                setCache[i] = values[in1] ^ values[in2]
        elif in1 in keys:
            if values[in1] == 1 and gate == "OR":
                setCache[i] = 1
            elif gate == "AND":
                setCache[i] = 0
        elif in2 in keys:
            if values[in2] == 1 and gate == "OR":
                setCache[i] = 1
            elif gate == "AND":
                setCache[i] = 0
        if i not in setCache.keys():
            variablePredicates.append(i)
    return setCache, variablePredicates, outputs
    
def extract_z_values(values):
    expected = parse_expected_out(values)
    nZ = len(bin(expected)) - 3 + 100 # Want two digit with leading zeros
    for i, b in enumerate(bin(expected)[2:]):
        zed = "z" + str(nZ - i)[1:]
        values[zed] = b
    return values

def check_valid(values, predicates):
    return True 

def main():
    # Extract data from files
    setValues = parse_init_values()
    setValues = extract_z_values(setValues)
    setPredicates = parse_predicates()
    while True:
        values = copy.deepcopy(setValues)
        predicates = copy.deepcopy(setPredicates)
        print("Input wires to swap:")
        swapMem = list()
        for i in range(1, 5):
            while True:
                try:
                    swap1, swap2 = input().split()
                    swap1 = int(swap1)
                    swap2 = int(swap2)
                    in11, in12, gate1, out1 = predicates[swap1]
                    in21, in22, gate2, out2 = predicates[swap2]
                    predicates[swap1] = (in11, in12, gate1, out2)
                    predicates[swap2] = (in21, in22, gate2, out1)
                    print(f"Swap {i} successful!")
                    swapMem.append((swap1, swap2))
                except:
                    print("Illegal swap attempt! Try again.")
                    continue
                break
        print("All swaps complete")
                

        if check_valid(values, predicates):
            print("Valid!")
            for swap in swapMem:
                print(f"{swap[0]}, {swap[1]}")

if __name__ == "__main__":
    main()
