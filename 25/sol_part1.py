# itoombes, Advent of Code
# Day 25

DUMMY = 0
if DUMMY:
    INPUT = "input.txt"
else:
    INPUT = "dummy.txt"

def parse_input():
    keys = list()
    tumblr = list()
    lines = open(INPUT, "r").readlines()
    print(lines)
    i = 0
    while i < len(lines):
        line = lines[i].replace("\n", "")
        a = b = c = d = e = 0
        if line == "#####":
            for j in range(1, 6):
                if lines[i + j][0] == "#": a += 1
                if lines[i + j][1] == "#": b += 1
                if lines[i + j][2] == "#": c += 1
                if lines[i + j][3] == "#": d += 1
                if lines[i + j][4] == "#": e += 1
            print(f"K : {(a, b, c, d, e)}")
            keys.append((a, b, c, d, e))
        if line == ".....":
            for j in range(1, 6):
                print(lines[i + j])
                if lines[i + j][0] == "#": a += 1
                if lines[i + j][1] == "#": b += 1
                if lines[i + j][2] == "#": c += 1
                if lines[i + j][3] == "#": d += 1
                if lines[i + j][4] == "#": e += 1
            print(f"T : {(a, b, c, d, e)}")
            tumblr.append((a, b, c, d, e))
        i += 8
    print(tumblr)
    print(keys)
    return keys, tumblr

def main():
    keys, keyholes = parse_input()

if __name__ == "__main__":
    main()
