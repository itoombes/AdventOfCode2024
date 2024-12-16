# itoombes, Advent of Code 2024
# Day 16 
from enum import Enum
import heapq 
import copy
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
    def __str__(self): 
        return f"({self._score}, ({self._row}, {self._col}, {self._direction}))"
    def get_row(self): 
        return self._row
    def get_col(self):
        return self._col 
    def get_state(self):
        return (self._row, self._col, self._direction)
    def get_score(self): 
        return self._score
    def cw(self): 
        if self._direction == Compass.N: return Compass.E 
        if self._direction == Compass.E: return Compass.S 
        if self._direction == Compass.S: return Compass.W 
        if self._direction == Compass.W: return Compass.N 
    def ccw(self): 
        if self._direction == Compass.N: return Compass.W
        if self._direction == Compass.E: return Compass.N
        if self._direction == Compass.S: return Compass.E
        if self._direction == Compass.W: return Compass.S 
    def get_successors(self): # Update movement
        nextRow, nextCol = self._row, self._col 
        if self._direction == Compass.N: nextRow -= 1
        elif self._direction == Compass.E: nextCol += 1
        elif self._direction == Compass.S: nextRow += 1
        elif self._direction == Compass.W: nextCol -= 1

        # Return successors
        return [MazeNode(nextRow, nextCol, self._direction, self._score + 1),
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
        
        string = ""
        for line in self._maze:
            string += line + "\n"
        print(string)
    
    def heuristic(self, row, col):
        dr = self._end[0] - row
        if dr < 0: dr *= -1
        dc = self._end[1] - col
        if dc < 0: dc *= -1
        return dr + dc
    
    def astar_solve(self):
        initNode = MazeNode(self._start[0], self._start[1], Compass.E, 0)
        frontier = [(self.heuristic(initNode.get_row(), initNode.get_col()),initNode)]
        heapq.heapify(frontier)
        visited = {initNode.get_state() : initNode.get_score()}
        while len(frontier) > 0:
            _, node = heapq.heappop(frontier)
            print(str(node))
            # Check if end
            if node.get_row() == self._end[0] and node.get_col() == self._end[1]:
                return node.get_score()


            # Add unvisited and valid nodes, and lower cost visited nodes, to frontier
            successors = node.get_successors()
            for s in successors:
                # Ensure valid
                if self._maze[s.get_row()][s.get_col()] == "#":
                    continue
                
                # Check if not visited || visited at higher cost
                if s.get_state() not in visited.keys() or s.get_score() < visited[s.get_state()]:
                    visited[s.get_state()] = s.get_score()
                    heapq.heappush(frontier, (s.get_score() + self.heuristic(s.get_row(), s.get_col()), s))
        return None

    def get_best_paths(self):
        threshold = self.astar_solve()
        if threshold is None:
            print("NO VALID PATHS")
            return None
        print(f"Threshold is : {threshold}")
        input()
        # Perform a BFS search
        bestPathTiles = set()

        initNode = MazeNode(self._start[0], self._start[1], Compass.E, 0)
        frontier = [(set(), initNode),]
        visited = dict()
        while len(frontier) > 0:
            path, node = frontier.pop(0)
            path = copy.deepcopy(path)
            path.add(node.get_state()[0:2])
            print(node)
            # Check if end
            if node.get_row() == self._end[0] and node.get_col() == self._end[1]:
                for tile in path:
                    bestPathTiles.add(tile)
                continue
            # Ensure does not exceed path length
            if (node.get_score() + self.heuristic(node.get_row(), node.get_col())) > threshold:
                continue
            # Get successors
            for s in node.get_successors():
                # Check if valid
                if self._maze[s.get_row()][s.get_col()] == "#":
                    continue
                # Avoid paths that are longer than existing paths 
                if s.get_state() not in visited.keys() or s.get_score() <= visited[s.get_state()]:
                    visited[s.get_state()] = s.get_score()
                    frontier.append((path, s))
        
        for r, c in bestPathTiles:
            self._maze[r] = self._maze[r][:c] + "O" + self._maze[r][c + 1:]
        for line in self._maze:
            print(line)

        print(len(bestPathTiles))



def main():
    maze = Maze(INPUT)
    input()
    print(maze.get_best_paths())

if __name__ == "__main__":
    main()
