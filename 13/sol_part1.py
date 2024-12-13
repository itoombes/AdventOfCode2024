# itoombes, Advent of Code 2024
# Day 13

DUMMY = "dummyinput.txt"
INPUT = "input.txt"

class Machine:
    def __init__(self, ax, ay, bx, by, px, py):
        self._ax = ax
        self._ay = ay
        self._bx = bx
        self._by = by
        self._px = px
        self._py = py

    def __str__(self):
        string = f"Button A: X+{self._ax}, Y+{self._ay}\n"
        string += f"Button B: X+{self._bx}, Y+{self._by}\n"
        string += f"Prize: X={self._px}, Y={self._py}\n"
        return string

def extract_machines(file):
    f = open(file, "r")
    lines = f.readlines()
    machines = list()
    # Extract machines from the file
    i = 0
    while i < len(lines):
        ax = int(lines[i][12:14])
        ay = int(lines[i][18:20])
        i += 1
        bx = int(lines[i][12:14])
        by = int(lines[i][18:20])
        i += 1
        prize = lines[i][9:]
        prize = prize.split(",")
        px = int(prize[0])
        py = int(prize[1][3:])
        i += 2
        machines.append(Machine(ax, ay, bx, by, px, py))
    return machines


def main():
    for machine in extract_machines(INPUT):
        print(str(machine))

if __name__ == "__main__":
    main()
