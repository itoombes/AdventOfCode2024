# itoombes, Advent of Code 2024
# Day 18

import heapq

DUMMY = 1
INPUT_FILE = "input.txt"
DUMMY_FILE = "dummyinput.txt"
INPUT_CAPACITY = 71 
DUMMY_CAPACITY = 7
DUMMY_BYTES = 12
INPUT_BYTES = 1024

class World():
    def __init__(self, file, capacity, nBytes):
        self._corrupted = World.get_corrupted_bytes(file, nBytes)
        self._capacity = capacity 

    def get_corrupted_bytes(file, size):
        f = open(file, "r")
        lines = f.readlines()
        corrupted = list()
        for i in range(0, size):
            x, y = lines[i].split(",")
            x = int(x)
            y = int(y)
            corrupted.append((x, y))
        return corrupted 

    def heuristic(self, coords):
        x, y = coords
        # Want distance to final walls
        # So, x <= self._capacity, y <= self._capacity
        dx = self._capacity - x - 1
        dy = self._capacity - y - 1
        return dx + dy

    def get_adjacent(self, cost, coords):
        x, y = coords
        adjacent = list()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nx < 0 or ny < 0 or nx >= self._capacity or ny >= self._capacity:
                if (nx, ny) not in self._corrupted:
                    adjacent.append((cost + 1, (nx, ny)))
        return adjacent

    def astar_solve(self):
        # Tuples in form (<path cost>, (<x>, <y>))
        start = (0, (0, 0))
        frontier = [(self.heuristic(start[1]), start)]
        heapq.heapify(frontier)
        visited = {start[1] : 0}
        while len(frontier) > 0:
            _, node = heapq.heappop(frontier)
            print(node)
            # Check if goal
            if node[1] == (self._capacity, self._capacity):
                return node[0]
            # Add successors with lower path costs || unvisited to frontier
            successors = self.get_adjacent(node[0], node[1])
            for s in successors:
                if s[1] not in visited.keys() or s[0] < visited[s[1]]:
                    visited[s[1]] = s[0]
                    heapq.heappush(frontier, (s[0] + self.heuristic(s[1]), s))
        return None

    def __str__(self):
        strings = ["." * self._capacity] * self._capacity
        print(len(strings))
        print(len(strings[0]))
        for x, y in self._corrupted:
            strings[y] = strings[y][:x] + "#" + strings[y][x+1:]
        out = ""
        for string in strings:
            out += string + "\n"
        return out

def main():
    if DUMMY:
        world = World(DUMMY_FILE, DUMMY_CAPACITY, DUMMY_BYTES)
    else:
        world = World(INPUT_FILE, INPUT_CAPACITY, INPUT_BYTES)
    print(world)
    print(world.astar_solve())

if __name__ == "__main__":
    main()
