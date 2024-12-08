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

def main():
    nRows, nCols, freqs = parse_map()
    print(nRows, nCols, freqs)


if __name__ == "__main__":
    main()

