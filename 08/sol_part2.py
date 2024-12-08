# itoombes, Advent of Code 2024
# Day 8

import math

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
            # Extract point with lowest 'x', get dx and dy
            if antennae[i][0] < antennae[j][0]:
                initX = antennae[i][0]
                initY = antennae[i][1]
                dx = antennae[j][0] - initX
                dy = antennae[j][1] - initY
            else:
                initX = antennae[j][0]
                initY = antennae[j][1]
                dx = antennae[i][0] - initX
                dy = antennae[i][1] - initY
            divisor = math.gcd(dx, dy)
            dx = dx // divisor
            dy = dy // divisor
            print(f"\t\t({initX}, {initY}), dx : {dx}, dy : {dy}")
            # Add every candidate with lower x
            x = initX
            y = initY
            candidates.append((x, y))
            while True:
                x -= dx
                y -= dy
                if (x < 0) or (y < 0) or (y >= nRows):
                    break
                candidates.append((x, y))
            x = initX
            y = initY
            while True:
                x += dx
                y += dy
                if (x >= nCols) or (y < 0) or (y >= nRows):
                    break
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

