# itoombes, Advent of Code 2024
# Day 18

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

if __name__ == "__main__":
    main()
