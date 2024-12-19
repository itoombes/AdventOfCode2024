# itoombes, Advent of Code 2024
# Day 19

DUMMY = 0

if DUMMY:
    PATTERNS = "dummy1.txt"
    DESIGNS = "dummy2.txt"
else:
    PATTERNS = "input1.txt"
    DESIGNS = "input2.txt"

def extract_data(pattern_file, design_file):
    patterns = list()
    for pattern in open(pattern_file, "r").readline().split(" ,"):
        patterns.append(pattern.replace("\n", ""))
    designs = list()
    for line in open(design_file, "r").readlines():
        designs.append(line.replace("\n", ""))
    print(patterns)
    print(designs)


def main():
    extract_data(PATTERNS, DESIGNS)

if __name__ == "__main__":
    main()
