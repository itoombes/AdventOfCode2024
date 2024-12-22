# itoombes, Advent of Code
# Day 21 Part 2

import copy
#   ^ A
# < v >
ROBOT_PAD = {(0, 0) : "<",
             (1, 0) : "v",
             (2, 0) : ">",
             (1, 1) : "^",
             (2, 1) : "A"}
# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
KEYPAD = {(1, 0) : "0",
          (2, 0) : "A",
          (0, 1) : "1",
          (1, 1) : "2",
          (2, 1) : "3",
          (0, 2) : "4",
          (1, 2) : "5",
          (2, 2) : "6",
          (0, 3) : "7",
          (1, 3) : "8",
          (2, 3) : "9"}

def read_sequences():
    f = open("input.txt", "r")
    sequences = list()
    for line in f.readlines():
        sequence = list()
        for c in line.replace("\n", ""):
            sequence.append(c)
        sequences.append(sequence)
    return sequences

def extract_number(sequence):
    string = ""
    for c in sequence[:3]:
        string += c
    return int(string)

class RobotChain:
    def __init__(self, arms):
        self._arms = arms

    def move_up(self, i = 0):
        x, y = self._arms[i]
        if (x, y + 1) in ROBOT_PAD.keys():
            return RobotChain(self._arms[:i] + [(x, y + 1),] + self._arms[i + 1:])
        return None

    def move_left(self, i = 0):
        x, y = self._arms[i]
        if (x - 1, y) in ROBOT_PAD.keys():
            return RobotChain(self._arms[:i] + [(x - 1, y),] + self._arms[i + 1:])
        return None

    def move_down(self, i = 0):
        x, y = self._arms[i]
        if (x, y - 1) in ROBOT_PAD.keys():
            return RobotChain(self._arms[:i] + [(x, y - 1),] + self._arms[i + 1:])
        return None

    def move_right(self, i = 0):
        x, y = self._arms[i]
        if (x + 1, y) in ROBOT_PAD.keys():
            return RobotChain(self._arms[:i] + [(x + 1, y),] + self._arms[i + 1:])
        return None

    def action(self, i = 0):
        # Don't want to apply last arm's action
        if i == len(self._arms):
            print("LAST ARM ACTION!")
            return None
        action = ROBOT_PAD[self._arms[i]]
        if action == "A": return self.action(i + 1)
        elif action == "^": return self.move_up(i + 1)
        elif action == "<": return self.move_left(i + 1)
        elif action == "v": return self.move_down(i + 1)
        elif action == ">": return self.move_right(i + 1)
    
    def __str__(self):
        return str(self._arms)

    def get_state(self):
        return tuple(self._arms)

    def __eq__(self, other):
        return self.get_state() == other.get_state()

    def get_successors(self):
        candidates = (self.move_up(), self.move_down(), self.move_right(), self.move_left(), self.action())
        successors = list()
        for c in candidates:
            if c is not None:
                successors.append(c)
        return successors

def cost_between_states(chain, state):
    frontier = [(0, chain),]
    visited = set()
    visited.add(chain.get_state())
    while len(frontier) > 0:
        cost, node = frontier.pop(0)

def preprocess():
    pass

def main():
    chain = RobotChain([(2, 1), (0,0), (2,1)])
    print(chain.get_state())
    print()
    for s in chain.get_successors():
        print(s.get_state())
    return None

    while True:
        print(chain)
        x = input()
        if x == ",": nchain = chain.move_up()
        elif x == "a": nchain = chain.move_left()
        elif x == "o": nchain = chain.move_down()
        elif x == "e": nchain = chain.move_right()
        elif x == ".": nchain = chain.action()
        if nchain is not None:
            chain = nchain
        else:
            print("Illegal move")

if __name__ == "__main__":
    main()
