# itoombes, Advent of Code 2024
# Day 21

import copy

ROBOT_PAD = [[None, "^", "A"],
             ["<", "v", ">"]]
KEYPAD = [["7", "8", "9"],
          ["4", "5", "6"],
          ["1", "2", "3"],
          [None, "0", "A"]]


DUMMY = 1
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
    def __init__(self, bot1_r, bot1_c, bot2_r, bot2_c, bot3_r, bot3_c, output):
        self._bot1_r = bot1_r
        self._bot1_c = bot1_c
        self._bot2_r = bot2_r
        self._bot2_c = bot2_c
        self._bot3_r = bot3_r
        self._bot3_c = bot3_c
        self._output = output
    
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

    def get_successors(self):
        
        # Go thru each potential action sequence
        successors = list()
        # Directional button press 
        r = self._bot1_r
        c = self._bot1_c
        for row, col in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if row == 0 and col == 0:
                continue
            if row < 0 or row > 1:
                continue
            if col < 0 or col > 2:
                continue
            successors.append(BotChain(row, col, self._bot2_r, self._bot2_c, self._bot3_r, self._bot3_c, copy.copy(self._output)))
        # Action button press
        # Note that it modifies THIS OBJECT
        bot2_response = ROBOT_PAD[self._bot1_r][self._bot1_c]
        # Bot 2 directional response
        if bot2_response == "^":
            self._bot2_r -= 1
        elif bot2_response == "v":
            self._bot2_r += 1
        elif bot2_response == "<":
            self._bot2_c -= 1
        elif bot2_response == ">":
            self._bot2_c += 1
        if self.check_panic(): # Ensure bot 2 is pointing at valid location
            return successors
        # Bot 2 action response
        if bot2_response == "A":
            # Bot 3 directional response
            bot3_response = ROBOT_PAD[self._bot2_r][self._bot2_c]
            if bot3_response == "^":
                self._bot3_r -= 1
            elif bot3_response == "v":
                self._bot3_r += 1
            elif bot3_response == "<":
                self._bot3_c -= 1
            elif bot3_response == ">":
                self._bot3_c += 1
            if self.check_panic():
                return successors
            # Bot 3 action response
            if bot3_response == "A":
                self._output.append(KEYPAD[self._bot3_r][self._bot3_c])
        successors.append(self) 
        return successors


    def __str__(self):
        string = f"Bot 1 : ({self._bot1_r}, {self._bot1_c}) -> {ROBOT_PAD[self._bot1_r][self._bot1_c]}\n"
        string += f"Bot 2 : ({self._bot2_r}, {self._bot2_c}) -> {ROBOT_PAD[self._bot2_r][self._bot2_c]}\n"
        string += f"Bot 3 : ({self._bot3_r}, {self._bot3_c}) -> {KEYPAD[self._bot3_r][self._bot3_c]}\n"
        string += f"Output : {self._output}\n"
        return string

    def get_state(self):
        return (self._bot1_r, self._bot1_c, self._bot2_r, self._bot2_c, self._bot3_r, self._bot3_c, str(self._output))

    def get_output(self):
        return self._output

    def __eq__(self, other):
        return self.get_state() == other.get_state()

def solve_bfs(sequence):
    # Setup init node
    start = BotChain(0, 2, 0, 2, 3, 2, list())
    frontier = [(0, start),]
    visited = set()
    visited.add(start.get_state())

    while len(frontier) > 0:
        cost, chain = frontier.pop(0)
        cost += 1
        # Note that validity checked within each node
        for s in chain.get_successors():
            if s.get_state() in visited:
                continue
            visited.add(s.get_state())
            output = s.get_output()
            # Detect end
            if output == sequence:
                return cost
            # Ensure pattern is valid
            if output == sequence[:len(output)]:
                frontier.append((cost, s))
        
def extract_number(sequence):
    string = ""
    for c in sequence[:3]:
        string += c
    return int(string)

def main():
    count = 0
    for sequence in read_sequences():
        minMoves = solve_bfs(sequence)
        number = extract_number(sequence) 
        print(f"{sequence}: {minMoves} * {number}")
        count += minMoves * number
    print(count)


if __name__ == "__main__":
    main()
