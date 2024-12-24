# itoombes, Advent of Code 2024
# Day 24

DUMMY = 0
TEST = 0
if DUMMY:
    VALUES = "dummy1.txt"
    PREDICATES = "dummy2.txt"
elif TEST:
    VALUES = "test1.txt"
    PREDICATES = "test2.txt"
else:
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
    predicates = parse_predicates()
    values = apply_predicates(values, predicates)
    out = 0
    for k in values.keys():
        if k[0] == "z":
            print(f"{k}, {values[k]}")
            out = out | (values[k] << int(k[1:]))
    print(out)

if __name__ == "__main__":
    main()
