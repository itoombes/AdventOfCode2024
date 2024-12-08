# itoombes, Advent of Code 2024
# Day 8

def parse_map():
    grid = open("dummyinput.txt", "r").readlines()
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

            print(f"\t({initX}, {initY}), dx : {dx}, dy : {dy}")
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

