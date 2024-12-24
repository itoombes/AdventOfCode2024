# itoombes, Advent of Code 2024
# Day 24

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
    for k in values.keys():
        if k[0] == "x":
            x |= (values[k] << int(k[1:]))
        elif k[0] == "y":
            y |= (values[k] << int(k[1:]))
    print(bin(x))
    print(bin(y))
    return x + y


def parse_predicates():
    f = open(PREDICATES, "r")
    predicates = list()
    for line in f.readlines():
        line = line.replace("\n", "")
        in1, gate, in2, _, out = line.split(" ")
        predicates.append((in1, in2, gate, out))
    return predicates

def main():
    values = parse_init_values()
    print(values)
    expected = parse_expected_out(values)
    print(bin(expected))
    predicates = parse_predicates()

if __name__ == "__main__":
    main()
