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
    candidates = list()
    for i in range(0, len(antennae) - 1):
        for j in range(i + 1, len(antennae)):
            print(f"\t{antennae[i]}, {antennae[j]}")
            dx = antennae[j][0] - antennae[i][0]
            dy = antennae[j][1] - antennae[i][1]
            x1 = antennae[j][0] + dx
            x2 = antennae[i][0] - dx
            y1 = antennae[j][1] + dy
            y2 = antennae[i][1] - dy
            print(f"\t\t({x1},{y1}), ({x2}, {y2})")
            
            if (x1 >= 0) and (x1 <= nCols) and (y1 >= 0) and (y1 <= nRows):
                candidates.append((x1, y1))
            if (x2 >= 0) and (x2 <= nCols) and (y2 >= 0) and (y2 <= nRows):
                candidates.append((x2, y2))
    return candidates

def main():
    nRows, nCols, freqs = parse_map()
    print(nRows, nCols, freqs)
    locations = list()
    # Get antinode locations
    for f in freqs:
        print(f"{f}:")
        candidates = locate_antinodes(nRows, nCols, freqs[f])
        for candidate in candidates:
            if candidate not in locations:
                locations.append(candidate)
    print(len(locations))

if __name__ == "__main__":
    main()

