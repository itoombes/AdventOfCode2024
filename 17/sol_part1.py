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
        self._out = list()

    def run(self):
        while True:
            print(f"Register A: {self._A}")
            print(f"Register B: {self._B}")
            print(f"Register C: {self._C}")
            print(f"Program: {self._opcodes}")
            print(f"Opcount: {self._opcount}")
            print(f"Output: {self._out}")
            input()
            self.next_instruction()
    
    def next_instruction(self):
        if self._opcount >= len(self._opcodes) - 1:
            print("HALT!")
            exit()
        opcode = self._opcodes[self._opcount]
        self._opcount += 1
        if opcode == 0: self.adv()
        elif opcode == 1: self.bxl()
        elif opcode == 2: self.bst()
        elif opcode == 3: self.jnz()
        elif opcode == 4: self.bxc()
        elif opcode == 5: self.out()
        elif opcode == 6: self.bdv()
        elif opcode == 7: self.cdv()
        else: raise ValueError(f"Illegal opcode! {opcode}")

    def get_combo_operand(self):
        operand = self._opcodes[self._opcount]
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

    def get_literal_operand(self):
        self._opcount += 1
        return self._opcodes[self._opcount - 1]

    def adv(self):
        # Perform division
        self._A = self._A // (2 ** self.get_combo_operand()) 

    def bxl(self):
        # Bitwise XOR
        self._B ^= self.get_literal_operand()

    def bst(self):
        # Modulo 8
        self._B = self.get_combo_operand() % 8

    def jnz(self):
        if self._A == 0:
            return
        self._opcount = self.get_literal_operand()

    def bxc(self):
        _ = self.get_literal_operand()
        self._B ^= self._C

    def out(self):
        self._out.append(self.get_combo_operand() % 8)

    def bdv(self):
        self._B = self._A // (2 ** self.get_combo_operand())

    def cdv(self):
        self._C = self._B // (2 ** self.get_combo_operand())


def main():
    a, opcodes = read_from_file(INPUT)
    machine = Machine(a, opcodes)
    machine.run()

if __name__ == "__main__":
    main()
