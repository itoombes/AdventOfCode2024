# itoombes, Advent of Code
# Day 21 Part 2

import copy

ROBOT_PAD = ((None, "^", "A"),
             ("<", "v", ">"))
KEYPAD = (("7", "8", "9"),
          ("4", "5", "6"),
          ("1", "2", "3"),
          (None, "0", "A"))

class MultiArmedBotbit:
    def __init__(self, arms, lastArm):
        self._arms = arms # Pointers to each pad controlled by robot arm; 25 items
        self._lastArm = lastArm

    def move_up(self, i = 0):
        r, c = self._arms[i]
        if r == 0 or ROBOT_PAD[r - 1][c] is None:
            return None
        return MultiArmedBotbit(self._arms[:i] + [(r - 1, c),] + self._arms[i + 1:], self._lastArm)

    def move_down(self, i = 0):
        r, c = self._arms[i]
        if r == 1 or ROBOT_PAD[r + 1][c] is None:
            return None
        return MultiArmedBotbit(self._arms[:i] + [(r + 1, c),] + self._arms[i + 1:], self._lastArm)

    def move_left(self, i = 0):
        r, c = self._arms[i]
        if c == 0 or ROBOT_PAD[r][c - 1] is None:
            return None
        return MultiArmedBotbit(self._arms[:i] + [(r, c - 1),] + self._arms[i + 1:], self._lastArm)

    def move_right(self, i = 0):
        r, c = self._arms[i]
        if c == 2 or ROBOT_PAD[r][c + 1] is None:
            return None
        return MultiArmedBotbit(self._arms[:i] + [(r, c + 1),] + self._arms[i + 1:], self._lastArm)

    def handle_last_action(action):
        r, c = self._lastArm
        if action == "^":
            r -= 1
        elif action == "v":
            r += 1
        elif action == ">":
            c += 1
        elif action == "<":
            c -= 1
        if c < 0 or r < 0 or c > 2 or c > 3 or KEYPAD[r][c] == None:
            return None
        return MultiArmedBotbit(copy.copy(self._arms), (r, c))

    def action(self, i = 0):
        r, c = self._arms[i]
        action = ROBOT_PAD[r][c]
        
        # Handle last arm
        if i == len(self._arms) - 1:
            if action == "A": # DON'T HANDLE OUTPUT HERE
                return None
            return self.handle_last_arm(action)

        if action == "A":
            return self.action(i + 1)
        elif action == "^":
            return self.move_up(i + 1)
        elif action == "v":
            return self.move_down(i + 1)
        elif action == "<":
            return self.move_left(i + 1)
        elif action == ">":
            return self.move_right(i + 1)

    def get_successors(self):
        candidates = (self.move_up(), self.move_down(), self.move_right(), self.move_left(), self.action())
        successors = list()
        for c in candidates:
            if c is not None:
                successors.append(c)
        return successors

    def get_arms(self):
        return self._arms

    def get_state(self):
        return f"{self._arms}; {self._lastArm}"

    def __str__(self):
        return self.get_state()

    def get_last_arm(self):
        return self._lastArm

    def __eq__(self, other):
        return self.get_state() == other.get_state()

def moves_to_state(init, target):
    # Returns number of moves where last arm is at target, all others on "A"
    frontier = [(0, init),]
    visited = set()
    visited.add(init.get_state())
    while len(frontier) > 0:
        cost, chain = frontier.pop(0)
        cost += 1
        for s in chain.get_successors():
            print(s)
            if s.get_state() in visited:
                continue
            visited.add(s.get_state())
            # Check if end
            if chain.get_last_arm() == target:
                match = True
                for arm in chain.get_arms():
                    if arm != (0, 2):
                        match = False
                        break
                if match:
                    return cost
            # Add to frontier
            frontier.append((cost, chain))

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

def main():
    chain = MultiArmedBotbit([(0, 2),] * 25, (0,2))
    print(moves_to_state(chain, (0, 1)))


if __name__ == "__main__":
    main()
