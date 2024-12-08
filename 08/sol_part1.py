# itoombes, Advent of Code 2024
# Day 8

def parse_map():
    grid = open("input.txt", "r").readlines()
    # Get grid
    nRows = len(grid)
    nCols = len(grid[0]) - 1
    # Locate the frequencies and positions
    freqs = dict()
    for r, line in enumerate(grid):
        line = line.replace("\n", "")
        for c in range(0, nRows):
            char = line[c]
            if char != '.':
                if char in freqs:
                    freqs[char].append((r, c))
                else:
                    freqs[char] = [(r, c),]
    return (nRows, nCols, freqs)

def locate_antinodes(nRows, nCols, antennae):
    # Iterate from first to second last antenna
    for i in range(0, len(antennae) - 1):
        for j in range(i + 1, len(antennae)):
            print(f"\t{antennae[i]}, {antennae[j]}")

def main():
    nRows, nCols, freqs = parse_map()
    print(nRows, nCols, freqs)
    locations = list()
    # Get antinode locations
    for f in freqs:
        print(f)
        candidates = locate_antinodes(nRows, nCols, freqs[f])

if __name__ == "__main__":
    main()

