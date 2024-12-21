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
        action = self._arms[r][c]
        
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
    botbit = MultiArmedBotbit

if __name__ == "__main__":
    main()
