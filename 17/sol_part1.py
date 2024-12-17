# itoombes, Advent of Code 2024
# Day 17

INPUT = "input.txt"
DUMMY = "dummyinput.txt"
DEBUG = True

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
            if DEBUG:
                print(f"Register A: {self._A}")
                print(f"Register B: {self._B}")
                print(f"Register C: {self._C}")
                print(f"Program: {self._opcodes}")
                print(f"Opcount: {self._opcount} | {self._opcodes[self._opcount]}")
            print(f"Output: {self._out}")
            if DEBUG:
                input()
            self.next_instruction()
            if self._opcount < 0 or self._opcount >= len(self._opcodes) - 1:
                print("Halt")
                return
    
    def next_instruction(self):
        # Extract current opcode
        opcode = self._opcodes[self._opcount]
        self._opcount += 1
        # Extract operands
        literal = self._opcodes[self._opcount]
        combo = self.get_combo_operand() # Increments opcount
        # Repeated math
        div = self._A // (2 ** combo) 
        mod = combo % 8

        if DEBUG:
            print(f"Literal : {literal}, Combo : {combo}")
        # Opcode instructions
        if opcode == 0: # ADV
            if DEBUG: print("ADV")
            self._A = div
        elif opcode == 1: # BXL
            if DEBUG: print("BXL")
            self._B = self._B ^ literal
        elif opcode == 2: # BST
            if DEBUG: print("BST")
            self._B = mod
        elif opcode == 3: # JNZ
            if DEBUG: print("JNZ")
            if self._A != 0:
                self._opcount = literal
        elif opcode == 4: # BXC
            if DEBUG: print("BXC")
            self._B = self._B ^ self._C
        elif opcode == 5: # OUT
            if DEBUG: print("OUT")
            self._out.append(mod) 
        elif opcode == 6: # BDV
            if DEBUG: print("BDV")
            self._B = div
        elif opcode == 7: # CDV
            if DEBUG: print("CDV")
            self._C = div
        else:
            raise ValueError(f"Illegal opcode! {opcode}")

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

def main():
    a, opcodes = read_from_file(INPUT)
    machine = Machine(a, opcodes)
    machine.run()

if __name__ == "__main__":
    main()
