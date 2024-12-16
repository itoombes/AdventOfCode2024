# itoombes, Advent of Code 2024
# Day 16

# Input
MAZE_0 = "input.txt"
MAZE_1 = "dummyinput.txt"
MAZE_2 = "testinput.txt"
INPUT = MAZE_1
# Chars
WALL = "#"
FREE = "."
START = "S"
END = "E"
# Directions
N = 0
E = 1
S = 2
W = 3
DEFAULT_DIR = E

class Maze():
    def __init__(self, file):
        self._maze, self._start = Maze.read_maze(file)
    
    def __str__(self):
        string = ""
        for r, row in enumerate(self._maze):
            string += row + "\n"
        return string

    def read_maze(file):
        f = open(file, "r")
        maze = list()
        start = end = None
        for r, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            if "S" in line:
                for c in range(0, len(line)):
                    if line[c] == START:
                        start = (r, c)
            maze.append(line)
        return (maze, start)
    
    def bfs_solve(self):
        # Storing nodes as (<parent>, <row>, <col>, <direction>, <explored>, <score>)
        frontier = [(None, self._start[0], self._start[1], DEFAULT_DIR, [(self._start[0], self._start[1], DEFAULT_DIR),], 0),]
        solutions = list() 
        while len(frontier) > 0:
            node = frontier.pop(0)
            parent, r, c, direction, explored, score = node
            # Go thru next steps 
            CW = CCW = None
            nextR, nextC = r, c
            if direction == N:
                CW = E
                CCW = W
                nextR -= 1
            elif direction == E:
                CW = S
                CCW = N
                nextC += 1
            elif direction == S:
                CW = W
                CCW = E
                nextR += 1
            elif direction == W:
                CW = N
                CCW = S
                nextC -= 1
            # Note will never be out of bounds - would hit a wall first
            # Note that if have one motion to solution, no possible shorter path
            # Check if solution
            if self._maze[nextR][nextC] == END:
                score += 1
                solutions.append(score)
                continue
            # If not part of solution and on map
            if self._maze[nextR][nextC] == FREE and (nextR, nextC, direction) not in explored:
                score += 1
                explored.append((nextR, nextC, direction))
                frontier.append((parent, nextR, nextC, direction, explored, score))
            # Add next directions
            score += 1000
            if (r, c, CW) not in explored:
                explored.append((r, c, CW))
                frontier.append((parent, r, c, CW, explored, score))
            if (r, c, CCW) not in explored:
                explored.append((r, c, CCW))
                frontier.append((parent, r, c, CCW, explored, score))
        print(solutions)


def main():
    maze = Maze(INPUT)
    print(maze)
    maze.bfs_solve()


if __name__ == "__main__":
    main()
