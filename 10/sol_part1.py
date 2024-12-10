# itoombes, Advent of Code 2024
# Day 10

TESTING = True

if TESTING:
    INPUT = "dummyinput.txt"
else:
    INPUT = "input.txt"

def parse_map(file):
    f = open(file, "r")
    trailheads = list()
    island = list()
    for r, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        island.append(line)
        if '0' in line:
            for c in range(0, len(line)):
                if line[c] == '0':
                    trailheads.append((r, c))
    return island, trailheads

def main():
    island, trailheads = parse_map(INPUT)
    print(island)
    print(trailheads)

if __name__ == "__main__":
    main()
