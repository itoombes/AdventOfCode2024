# itoombes, Advent of Code 2024
# Day 21

import copy

ROBOT_PAD = [[None, "^", "A"],
             ["<", "v", ">"]]
KEYPAD = [["7", "8", "9"],
          ["4", "5", "6"],
          ["1", "2", "3"],
          [None, "0", "A"]]


DUMMY = 0
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"

def read_sequences():
    f = open(INPUT, "r")
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

class MultiArmedBotbit:
    def __init__(self, firstArm, midArms)
        self._firstArm = firstArm
        self._arms = midArms

    def get_successors(self):
        successors = list()
        r, c = self._firstArm
        # If motion in the first arm is applied
        for nR, nC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            # Ensure not (0,0)
            if nR == nC == 0:
                continue
            # Ensure in range
            if nR >= 0 and nR < 2 and nC >= 0 and nC < 3:
                successors.append(MultiArmedBotbit((nR, nC), copy.copy(self._arms), self._lastArm))
        # Action takes place - note this modifies self!
        action = ROBOT_PAD[r][c]
        # Update all arms but the last
        for i in range(0 , len(arms) - 1):
            # Handle motion - note that this terminates the update process
            if action != "A":
                nR, nC = self._arms[i]
                if action == "^":
                    if nR == 0 or nC == 0: # Skip moving when up or to (0, 0)
                        return successors
                    else:
                        nR -= 1
                elif action == "<":
                    if (nR == 1 and nC == 1) or nC == 0:
                        return successors
                    else:
                        nC -= 1
                elif action == ">":
                    if nC == 2:
                        return successors
                    else:
                        nC += 1
                elif action == "v":
                    if nR == 1:
                        return successors
                    else:
                        nR += 1
                # Don't process any more arms
                self._arms[i] = (nR, nC)
                successors.append(self)
                return successors




    def get_last_arm(self):
        return self._arms[-1]

    def __str__(self):
        return f"{self._firstArm}, {str(self._arms)}, {self._lastArm}\n"
        
    def __eq__(self, other):
        return str(self) == str(other)

    def update_from_start(self):
        pass


def main():
    MultiArmedBotbit((0, 2), [(0, 2),] * 24)
    

if __name__ == "__main__":
    main()
