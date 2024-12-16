# itoombes, Advent of Code 2024
# Day 16

import heapq

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

class MazeNode():
    def __init__(self, row, col, direction, cost):
        self._row = row
        self._col = col
        self._dir = direction
        self._cost = cost

    def get_row(self):
        return self._row
    
    def get_col(self):
        return self._col

    def get_state(self):
        return (self._row, self._col, self._dir)

    def get_cost(self):
        return self._cost

    def get_successors(self):
        successors = list()
        if self._dir == N:
            return [MazeNode(self._row - 1, self._col, N, self._cost + 1),
                    MazeNode(self._row, self._col, W, self._cost + 1000),
                    MazeNode(self._row, self._col, E, self._cost + 1000)]
        elif self._dir == E:
            return [MazeNode(self._row - 1, self._col, E, self._cost + 1),
                    MazeNode(self._row, self._col, N, self._cost + 1000),
                    MazeNode(self._row, self._col, S, self._cost + 1000)]
        elif self._dir == S:
            return [MazeNode(self._row - 1, self._col, S, self._cost + 1),
                    MazeNode(self._row, self._col, W, self._cost + 1000),
                    MazeNode(self._row, self._col, E, self._cost + 1000)]
        elif self._dir == W:
            return [MazeNode(self._row - 1, self._col, W, self._cost + 1),
                    MazeNode(self._row, self._col, S, self._cost + 1000),
                    MazeNode(self._row, self._col, N, self._cost + 1000)]

    def __lt__(self, other):
        return self.get_cost() < other.get_cost()


class Maze():
    def __init__(self, file):
        self._maze, self._start, self._end = Maze.read_maze(file)
    
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
            elif "E" in line:
                for c in range(0, len(line)):
                    if line[c] == END:
                        end = (r, c)
            maze.append(line)
        return (maze, start, end)
    
    def manhatten_distance(self, row, col):
        rDist = self._end[0] - row
        if rDist < 0: rDist *= -1
        cDist = self._end[1] - col
        if cDist < 0: cDist *= -1
        return rDist + rDist

    def solve(self):
        # Based on Univesity of Queensland COMP3702 A* Code
        initNode = MazeNode(self._start[0], self._start[1], DEFAULT_DIR, 0)
        frontier = [(0, initNode),]
        heapq.heapify(frontier)
        visited = {initNode.get_state() : 0}
        while len(frontier) > 0:
            _, node = heapq.heappop(frontier)

            # Check if this node is the goal
            if node.get_row() == self._end[0] and node.get_col() == self._end[1]:
                return node.get_cost()
            # Add unvistied or visited at greater path cost successors
            successors = node.get_successors()
            for s in successors:
                if s.get_state() not in visited.keys() or s.get_cost() < visited[s.get_state()]:
                    visited[s.get_state()] = s.get_cost()
                    heapq.heappush(frontier,
                                   (s.get_cost() + self.manhatten_distance(s.get_row(), s.get_col()), s))
            


def main():
    maze = Maze(INPUT)
    print(maze)
    print(maze.solve())


if __name__ == "__main__":
    main()
