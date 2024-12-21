# itoombes, Advent of Code
# Day 21

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

def solve(sequence):
    print(sequence)
    return 0


def main():
    count = 0
    for sequence in read_sequences():
        minMoves = solve(sequence)
        number = extract_number(sequence)
        print(f"{sequence}: {minMoves} * {number}")
        count += minMoves * number
        input()
    print(count)

if __name__ == "__main__":
    main()
