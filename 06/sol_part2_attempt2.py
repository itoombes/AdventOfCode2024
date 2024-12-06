# itoombes, Advent of Code
# Day 6

import copy

def read_maze():
    f = open("input.txt", "r")
    lines = list()
    for i, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        if "^" in line:
            row = i
            j = 0
            while True:
                if line[j] == "^":
                    col = j
                    break
                j += 1
        lines.append(line)
    return lines, col, j

def main():
    ogMaze, guardRow, guardCol = read_maze()
    nRows = len(ogMaze)
    nCols = len(ogMaze[0])
    
    count = 0

    # Iterate thru all possible squares
    for i in range(0, nRows):
        for j in range(0, nCols):
            print(f"({i}, {j})")
            if ogMaze[i][j] == "^":
                print("\tGuard location - skip")
                continue
            if ogMaze[i][j] == "#":
                print("\tAlready an obstacle - skip")
                continue

            # Generate the specific maze
            maze = copy.deepcopy(ogMaze)
            maze[i] = maze[i][0:j] + "#" + maze[i][j + 1:]

            # Go thru the maze, exiting if outside area or if reach loop
            row = guardRow
            col = guardCol
            visited = [(row, col, "u"),]
            orientation = "u"
            initCount = count
            while True:
                # Handle motion and rotation
                if orientation == "u":
                    if row == 0: # Out of bounds
                        break
                    row -= 1
                    if maze[row][col] == "#":
                        row += 1
                        orientation = "r"
                elif orientation == "r":
                    if col == nCols - 1: # Out of bounds
                        break
                    col += 1
                    if maze[row][col] == "#":
                        col -= 1
                        orientation = "d"
                elif orientation == "d":
                    if row == nRows - 1: # Out of bounds
                        break
                    row += 1
                    if maze[row][col] == "#":
                        row -= 1
                        orientation = "l"
                elif orientation == "l":
                    if col == 0: # Out of bounds
                        break
                    col -= 1
                    if maze[row][col] == "#":
                        col += 1
                        orientation = "u"
                # check if visited 
                if (row, col, orientation) in visited:
                    count += 1
                    break
                else:
                    visited.append((row, col, orientation))
            if initCount == count:
                print("\tOut of bounds")
            else:
                print("\tLoop!")
    print(count)            

if __name__ == "__main__":
    main()
