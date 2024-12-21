# itoombes, Advent of Code
# Day 21

KEYPAD = {"9" : (2, 0),
          "8" : (1, 0),
          "7" : (0, 0),
          "6" : (2, 1),
          "5" : (1, 1),
          "4" : (0, 1),
          "3" : (2, 2),
          "2" : (1, 2),
          "1" : (0, 2),
          "0" : (1, 3),
          "A" : (2, 3)}

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

def extract_min_path(sequence):
    p = (2, 3)
    moves = list()
    for c in sequence:
        c = KEYPAD[c]
        # Move up & to the right before move down & to the left
        # Avoids the empty corner
        while p[1] < c[1]:
            p = (p[0], p[1] + 1)
            moves.append("^")
        while p[0] < c[0]:
            p = (p[0] + 1, p[1])
            moves.append(">")
        while p[0] > c[0]:
            p = (p[0] - 1, p[1])
            moves.append("v")
        while p[0] < c[0]:
            p = (p[0] + 1, p[1])
            moves.append("<")
    return moves

def solve(sequence):
    print(sequence)
    bestKeypadPath = extract_min_path(sequence)
    print(bestKeypadPath)
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
