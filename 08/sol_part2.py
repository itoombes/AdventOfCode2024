# itoombes, Advent of Code 2024
# Day 8

def parse_map():
    grid = open("dummyinput2.txt", "r").readlines()
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
                    freqs[char].append((c, r))
                else:
                    freqs[char] = [(c, r),]
    return (nRows, nCols, freqs)

def locate_antinodes(nRows, nCols, antennae):
    # Iterate from first to second last antenna
    candidates = list()
    for i in range(0, len(antennae) - 1):
        for j in range(i + 1, len(antennae)):
            print(f"\t{antennae[i]}, {antennae[j]}")
            dx = antennae[j][0] - antennae[i][0]
            dy = antennae[j][1] - antennae[i][1]
            xmin = antennae[i][0]
            xmax = antennae[j][0]
            if dx < 0:
                xmin = antennae[j][0]
                xmax = antennae[i][0]
                dx *= -1
            ymin = antennae[i][1]
            ymax = antennae[j][1]
            if dy < 0:
                ymin = antennae[j][1]
                ymax = antennae[i][1]
                dy *= -1

            for x in range(xmin - dx, xmax + dx + 1):
                for y in range(ymin - dy, ymax + dy + 1):
                    if (x >= 0) and (y >= 0) and (x < nCols) and (y < nRows):
                        candidates.append((x, y))
    print(f"\t{candidates}")
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

