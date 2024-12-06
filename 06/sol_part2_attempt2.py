# itoombes, Advent of Code
# Day 6

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
    maze, guardRow, guardCol = read_maze()
    # Iterate thru all possible squares
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            print(f"({i}, {j})")
            if maze[i][j] == "^":
                print("\tGuard location - skip")
                continue
            if maze[i][j] == "#":
                print("\tAlready an obstacle - skip")
                continue

if __name__ == "__main__":
    main()
