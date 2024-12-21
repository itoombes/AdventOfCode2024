# itoombes, Advent of Code 2024
# Day 21

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

class BotChain():
    def __init__(self):
        # Bot 1 - user controlled, points to bot 2
        self._bot1_r = self._bot1_c = None
        # Bot 2 - controlled by bot 1, points to bot 3
        self._bot2_r = self._bot2_c = None
        # Bot 3 - controlled by bot 2, points to keypad
        self._bot3_r = self._bot3_c = None
        self._reset()

    def reset(self):
        self._bot1_r = 0
        self._bot1_c = 2
        self._bot2_r = 0
        self._bot2_c = 2
        self._bot3_r = 3
        self._bot3_c = 2
    
    def check_panic(self):
        # Check row position
        for row in ((self._bot1_r, self._bot2_r)):
            if row < 0 or row > 1:
                return True
        if self._bot3_r < 0 or self._bot3_r > 3:
            return True
        # Check column position
        for col in ((self._bot1_c, self._bot2_c, self._bot3_c)):
            if col < 0 or col > 2:
                return True
        return False

def main():
    print(read_sequences())
    control = BotChain()

if __name__ == "__main__":
    main()
