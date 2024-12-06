# itoombes, Advent of Code 2024
# Day 6

import copy

def parse_map():
    world = list()
    f = open("dummyinput.txt", "r")
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
    maxRow = len(world) - 1
    maxCol = len(world[0]) - 1

    print(world)
    # Parse thru the valid locations to place an obstacle in the first place
    while True:
        if orientation == "up":
            if row == 0: break
            if world[row - 1][col] == "#":
                orientation = "right"
            else:
                row -= 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "right":
            if col == maxCol: break
            if world[row][col + 1] == "#":
                orientation = "down"
            else:
                col += 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "down":
            if row == maxRow: break
            if world[row + 1][col] == "#":
                orientation = "left"
            else:
                row += 1
                if (row, col) not in visited:
                    visited.append((row, col))
        if orientation == "left":
            if col == 0: break
            if world[row][col - 1] == "#":
                orientation = "up"
            else:
                col -= 1
                if (row, col) not in visited:
                    visited.append((row, col))
    print(len(visited))
    
    # Now, iterate thru the 
    placements = copy.deepcopy(visited)

    # Brute force it - using existing placements doesn't work
    placements = list()
    i = 0
    while i <= maxRow:
        j = 0
        while j <= maxCol:
            placements.append((i, j))
            j += 1
        i += 1

    count = 0
    oldWorld = copy.deepcopy(world)
    for placement in placements:
        print(placement)
        if placement[0] == initRow and placement[1] == initCol:
            continue
        row = initRow
        col = initCol
        world = copy.deepcopy(oldWorld)
        world[placement[0]] = world[placement[0]][:placement[1]] + "#" + world[placement[0]][placement[1] + 1:]
        visited = [(row, col, "up"),]
        while True:
            if orientation == "up":
                if row == 0: break
                if world[row - 1][col] == "#":
                    orientation = "right"
                else:
                    row -= 1
                    if (row, col, orientation) in visited:
                        print("Match!")
                        count += 1
                        break
                    visited.append((row, col, orientation))
            elif orientation == "right":
                if col == maxCol: break
                if world[row][col + 1] == "#":
                    orientation = "down"
                else:
                    col += 1
                    if (row, col, orientation) in visited:
                        count += 1
                        print("Match!")
                        break
                    visited.append((row, col, orientation))
            elif orientation == "down":
                if row == maxRow: break
                if world[row + 1][col] == "#":
                    orientation = "left"
                else:
                    row += 1
                    if (row, col, orientation) in visited:
                        print("Match!")
                        count += 1
                        break
                    visited.append((row, col, orientation))
            elif orientation == "left":
                if col == 0: break
                if world[row][col - 1] == "#":
                    orientation = "up"
                else:
                    col -= 1
                    if (row, col, orientation) in visited:
                        print("Match!")
                        count += 1
                        break
                    visited.append((row, col, orientation))
    print(count)

if __name__ == "__main__":
    main()
