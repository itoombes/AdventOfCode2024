# itoombes, Advent of Code 2024
# Day 16

from enum import Enum
import heapq

# Inputs
MAZE_0 = "input.txt"
MAZE_1 = "dummyinput.txt"
MAZE_2 = "testinput.txt"
INPUT = MAZE_0

class Compass(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

class MazeNode():
    def __init__(self, row, col, direction, score):
        self._row = row
        self._col = col
        self._direction = direction
        self._score = score
    
    def get_row(self):
        return self._row

    def get_col(self):
        return self._col
    
    def get_state(self):
        return (self._row, self._col, self._direction)

    def get_score(self):
        return self._score

    def cw(self):
        if self.direction == Compass.N:
            return Compass.E
        if self.direction == Compass.E:
            return Compass.S
        if self.direction == Compass.S:
            return Compass.W
        if self.direction == Compass.W:
            return Compass.N
    def ccw(self):
        if self.direction == Compass.N:
            return Compass.W
        if self.direction == Compass.E:
            return Compass.N
        if self.direction == Compass.S:
            return Compass.E
        if self.direction == Compass.W:
            return Compass.S

    def get_successors(self):
        # Update movement
        nextRow, nextCol = self._row, self._col
        if self.direction == Compass.N:
            nextRow -= 1
        elif self.direction == Compass.E:
            nextCol += 1
        elif self.direction == Compass.S:
            nextRow += 1
        elif self.direction == Compass.W:
            nextCol -= 1

        # Return successors
        return [MazeNode(nextRow, nextCol, self.direction, self._score + 1),
                MazeNode(self._row, self._col, self.cw(), self._score + 1000),
                MazeNode(self._row, self._col, self.ccw(), self._score + 1000)]
    
    def __lt__(self, other):
        return self.get_score() < other.get_score()


class Maze():
    def __init__(self, file):
        """
        Parse the maze environment as a file
        Extracts maze, its start point, and its end point
        """
        f = open(file, "r")
        self._maze = list()
        for r, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            if "S" in line:
                for c in range(0, len(line)):
                    if line[c] == "S":
                        self._start = (r, c)
            elif "E" in line:
                for c in range(0, len(line)):
                    if line[c] == "E":
                        self._end = (r, c)
            self._maze.append(line)
    
    def solve(self):
        print((self._maze, self._start, self._end))


def main():
    maze = Maze(INPUT)
    print(maze.solve())

if __name__ == "__main__":
    main()
