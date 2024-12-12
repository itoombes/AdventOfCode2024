# itoombes, Advent of Code 2024
# Day 12

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
    regionAreas = list()
    # The size of each region, in same order as tiles
    perimeters = list()
    for r in range(0, len(farm)):
        for c in range(0, len(farm[0])):
            if (r, c) not in visited:
                newRegion, newPerimeter = grow_region(farm, r, c)
                for tile in newRegion:
                    visited.append(tile)
                regionAreas.append(len(newRegion))
                perimeters.append(newPerimeter)
    return regionAreas, perimeters

def grow_region(farm, row, col):
    print(f"Growing region from ({row}, {col})...")
    region = [(row, col),]
    perimeter = list()
    tileType = farm[row][col]
    frontier = [(row, col),]
    while len(frontier) != 0:
        r, c = frontier.pop()
        toAdd = list()
        # Get adjacent tiles, add to frontier
        # If any spot without neighbours, add to perimeter
        for nR, nC in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            #print(f"\t({nR}, {nC}) : ", end="")
            if (nR, nC) in region:
                #print("Already explored")
                continue
            if nR < 0 or nC < 0 or nR >= len(farm) or nC >= len(farm[0]):
                #print("Out of bounds")
                if (r, c) not in perimeter:
                    perimeter.append((r, c))
                continue
            if farm[nR][nC] == tileType:
                #print("New tile in region!")
                region.append((nR, nC))
                frontier.append((nR, nC))
            else:
                #print("Tile not in region")
                if (r, c) not in perimeter:
                    perimeter.append((r, c))
    return region, perimeter

def extract_sides(perimeter):
    print(perimeter)
    return 1

def main():
    farm = read_farm(DUMMY)
    regions, perimeters = parse_regions(farm)
    price = 0
    for i in range(0, len(regions)):
        price += regions[i] * extract_sides(perimeters[i])
    print(price)

if __name__ == "__main__":
    main()
