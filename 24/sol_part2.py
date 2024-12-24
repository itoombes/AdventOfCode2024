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

def confirm_valid(values, predicates, cache, outputs):
    # Set the cached values
    for i in cache.keys():
        if outputs[i][0] == "z" and cache[i] != values[outputs[i]]:
            return False
        else:
            values[outputs[i]] = cache[i]
    # 


def permutations(number):
    # Generate every swap index
    pairs = list()
    for i in range(0, number - 1):
        for j in range(i + 1, number):
            pairs.append((i, j))

    swaps = list()
    for i in range(0, len(pairs) - 3):
        print(i)
        for j in range(i, len(pairs) - 2):
            print(f"\t{j}")
            for k in range(j, len(pairs) - 1):
                print(f"\t{k}")
                for l in range(k, len(pairs)):
                    print(f"\t{l}")
                    swaps.append((pairs[i][0], pairs[i][1],
                                  pairs[j][0], pairs[j][1],
                                  pairs[k][0], pairs[k][1],
                                  pairs[l][0], pairs[l][1]))
                    
    print(pairs)

def main():
    # Extract data from files
    setValues = parse_init_values()
    setValues = extract_z_values(setValues)
    predicates = parse_predicates()
    cache, variablePredicates, outputs = sort_predicates(setValues, predicates)
    # Generate permutations
    for perm in permutations(len(predicates)):
        values = copy.deepcopy(setValues)
        variablePredicates = copy.deepcopy(variablePredicates)
        print(perm)

if __name__ == "__main__":
    main()
