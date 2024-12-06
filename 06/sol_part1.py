# itoombes, Advent of Code 2024
# Day 6


def parse_map():
    world = list()
    f = open("input.txt", "r")
    guardRow = 0
    guardCol = 0
    for i, line in enumerate(f.readlines()):
        line.replace("\n", "")
        if "^" in line:
            guardRow = i
            strLen = len(line)
            j = 0
            while j < strLen:
                if line[j] == "^":
                    guardCol = j
                    break
                j += 1
        world.append(line)
    return (world, guardRow, guardCol)

def main():
    # Establish the world
    world, row, col = parse_map()
    visited = [(row, col),]
    orientation = "up"
    nRows = len(world)
    nCols = len(world[0])

    # Go through the area
    while True:
        if orientation == "up":
            if world[row - 1][col] == "#":
                orientation = "right"
            else:
                row -= 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "right":
            if world[row][col + 1] == "#":
                orientation = "down"
            else:
                col += 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "down":
            if world[row + 1][col] == "#":
                orientation = "left"
            else:
                row += 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "left":
            if world[row][col - 1] == "#":
                orientation = "up"
            else:
                col -= 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if row == 0 or row == nRows - 1 or col == 0 or col == nCols - 1:
            break
    print(len(visited))



if __name__ == "__main__":
    main()
