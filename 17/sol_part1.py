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


def main():
    a, opcodes = read_from_file(INPUT)
    print(a)
    print(opcodes)

if __name__ == "__main__":
    main()
