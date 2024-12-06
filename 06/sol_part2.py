# itoombes, Advent of Code 2024
# Day 6

import copy

def parse_map():
    world = list()
    f = open("input.txt", "r")
    guardRow = 0
    guardCol = 0
    for i, line in enumerate(f.readlines()):
        if "^" in line:
            guardRow = i
            strLen = len(line)
            j = 0
            while j < strLen:
                if line[j] == "^":
                    guardCol = j
                    break
                j += 1
        world.append(line[:-1])
    return (world, guardRow, guardCol)

def main():
    # Establish the world
    world, initRow, initCol = parse_map()
    row, col = initRow, initCol
    visited = [(row, col, "up"),]
    orientation = "up"
    nRows = len(world)
    nCols = len(world[0])

    print(world)
    # Parse thru the valid locations to place an obstacle in the first place
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
    
    # Now, iterate thru the 
    placements = copy.deepcopy(visited)

    print(nCols)
    count = 0
    for placement in placements:
        # Skip placing at the initial guard point
        if placement[0] == initRow and placement[1] == initCol:
            continue
        # Establish the new placement of an obstacle
        newWorld = copy.deepcopy(world)
        newWorld[placement[0]] = world[placement[0]][:placement[1]] + '#' + world[placement[0]][placement[1] + 1:]
        # Iterate through the modified world, stopping if loop detected
        visited = [(initRow, initCol, "up"),]
        while True:
            if orientation == "up":
                if newWorld[row - 1][col] == "#":
                    orientation = "right"
                else:
                    row -= 1
                    if (row, col, orientation) not in visited:
                        visited.append((row, col, orientation))
                    else:
                        count += 1
                        break
            if orientation == "right":
                print(newWorld[row])
                print(col)
                if newWorld[row][col + 1] == "#":
                    orientation = "down"
                else:
                    col += 1
                    if (row, col, orientation) not in visited:
                        visited.append((row, col, orientation))
                    else:
                        count += 1
                        break
            if orientation == "down":
                if newWorld[row + 1][col] == "#":
                    orientation = "left"
                else:
                    row += 1
                    if (row, col, orientation) not in visited:
                        visited.append((row, col, orientation))
                    else:
                        count += 1
                        break
            if orientation == "left":
                if newWorld[row][col - 1] == "#":
                    orientation = "up"
                else:
                    col -= 1
                    if (row, col, orientation) not in visited:
                        visited.append((row, col, orientation))
                    else:
                        count += 1
                        break
            if row == 0 or row == nRows - 1 or col == 0 or col == nCols - 1:
                break
    print(count)

if __name__ == "__main__":
    main()
