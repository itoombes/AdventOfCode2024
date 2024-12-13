# itoombes, Advent of Code 2024
# Day 13

import numpy as np

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
    
    def get_presses(self):
        buttons = np.array([[self._ax, self._bx], [self._ay, self._by]])
        target = np.array([self._px, self._py])
        result = np.linalg.solve(buttons, target)
       # print(result)
       # print(np.round(result))
        A = np.round(result)[0]
        B = np.round(result)[1]
        if ((A * self._ax) + (B * self._bx) == self._px) and ((A * self._ay) + (B * self._by) == self._py):
    #       print((A, B))
            return (A, B)
        return None
        

    def get_cost(self):
        presses = self.get_presses()
        if presses is None:
            return 0
        else:
            return (presses[0] * 3) + (presses[1])
            
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
    cost = 0
    for machine in extract_machines(INPUT):
        cost += machine.get_cost()
    print(cost)

if __name__ == "__main__":
    main()
