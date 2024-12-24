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

def parse_values():
    f = open(VALUES, "r")
    values = dict()
    for line in f.readlines():
        values[line[0:3]] = line[-2:-1]
    print(values)

def parse_predicates():
    pass

def main():
    parse_values()

if __name__ == "__main__":
    main()
