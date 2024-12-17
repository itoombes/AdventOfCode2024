# itoombes, Advent of Code 2024
# Day 17

INPUT = "input.txt"
DUMMY = "dummyinput.txt"

def read_from_file(file):
    f = open(file, "r")
    lines = f.readlines()
    a = int(lines[0].split(" ")[2])
    # b, c = 0 for both input files
    opcodes = list()
    for c in lines[4].split(" ")[1].split(","):
        opcodes.append(int(c))
    return a, opcodes

class Machine():
    def __init__(self, a_reg, opcodes):
        self._A = a_reg
        self._B = 0
        self._C = 0
        self._opcodes = opcodes
        self._opcount = 0
    
    def next_instruction(self):
        opcode = self._opcodes[self._opcount]
        self._opcount += 1
        # TODO : Parse the opcode
        pass

    def get_combo_value(self):
        opcode = self._opcodes[self._opcount]
        self._opcount += 1
        if operand >= 0 and operand < 4:
            return operand
        if operand == 4:
            return self._A
        if operand == 5:
            return self._B
        if operand == 6:
            return self._C
        raise ValueError("Invalid combo value!")

    def adv(self):
        # Perform division
        self._A = self._A // (2 ** self.get_combo_value()) 

def main():
    machine = Machine(read_from_file(DUMMY))

if __name__ == "__main__":
    main()
