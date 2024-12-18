# itoombes, Advent of Code 2024
# Day 18

import copy

DUMMY = 0
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
        self._shortest_path = self.bfs_solve()

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

    def get_adjacent(self, coords):
        x, y = coords
        adjacent = list()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nx < 0 or ny < 0 or nx >= self._capacity or ny >= self._capacity:
                continue
            if (nx, ny) not in self._corrupted:
                adjacent.append((nx, ny))
        return adjacent

    def bfs_solve(self):
        # Return the coords of the elements in the shortest path
        start = (set(), (0, 0))
        frontier = [start,]
        visited = set()
        visited.add((0,0))
        
        while len(frontier) > 0:
            nodeVisited, coords = frontier.pop(0)
            nodeVisited.add(coords)
            # Detect end
            if coords == (self._capacity - 1, self._capacity - 1):
                return nodeVisited
            for s in self.get_adjacent(coords):
                if s not in visited:
                    print(f"Visited : {s}")
                    visited.add(s)
                    frontier.append((copy.deepcopy(nodeVisited), s))
        return None
            
    def get_path_len(self):
        return len(self._shortest_path)

    def __str__(self):
        strings = ["." * self._capacity] * self._capacity
        for x, y in self._corrupted:
            strings[y] = strings[y][:x] + "#" + strings[y][x+1:]
        for x, y in self._shortest_path:
            strings[y] = strings[y][:x] + "O" + strings[y][x+1:]
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
    print(world.get_path_len() - 1) # want steps, not tiles

if __name__ == "__main__":
    main()
