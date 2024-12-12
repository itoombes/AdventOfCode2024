# itoombes, Advent of Code 2024
# Day 12

import copy

DUMMY = "dummyinput.txt"
INPUT = "input.txt"

def read_farm(file):
    f = open(file, "r")
    farm = list()
    for line in f.readlines():
        farm.append(line.replace("\n",""))
    return farm

def parse_regions(farm):
    """
    Return a list of regions
    """
    # List of tiles that have been explored
    visited = list()
    # Each region as a list of tiles
    regions = list()
    # The size of each region, in same order as tiles
    perimeters = list()
    for r in range(0, len(farm)):
        for c in range(0, len(farm[0])):
            if farm[r][c] not in visited:
                newRegion, newPerimeter = grow_region(farm, r, c)
                input()
                for tile in newRegion:
                    visited.append(tile)
                regions.append(newRegion)
                perimeters.append(newPerimeter)
    return regions, perimeters

def grow_region(farm, row, col):
    print(f"Growing region from ({row}, {col})...")
    region = [(row, col),]
    perimeter = 0
    tileType = farm[row][col]
    frontier = [(row, col),]
    while len(frontier) != 0:
        r, c = frontier.pop()
        toAdd = list()
        # Get adjacent tiles, add to frontier
        # If any spot without neighbours, add to perimeter
        for nR, nC in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            print(f"\t({nR}, {nC}) : ", end="")
            if (nR, nC) in region:
                print("Already explored")
                break
            if nR > 0 and nC > 0 and nR < len(farm) - 1 and nC < len(farm[0]) - 1 and farm[nR][nC] == tileType:
                print("New & part of region!")
                region.append((nR, nC))
                frontier.append((nR, nC))
            else:
                print("Not part of region")
                perimeter += 1
    print(f"Region is:\n{region}")
    return region, perimeter

def main():
    farm = read_farm(DUMMY)
    regions, perimeters = parse_regions(farm)
    print(regions)
    print(perimeters)

if __name__ == "__main__":
    main()
