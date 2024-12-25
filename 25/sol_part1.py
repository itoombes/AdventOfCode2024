# itoombes, Advent of Code
# Day 25

DUMMY = 0
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"

def parse_input():
    keys = list()
    tumblr = list()
    lines = open(INPUT, "r").readlines()
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
            keys.append((a, b, c, d, e))
        if line == ".....":
            for j in range(1, 6):
                if lines[i + j][0] == "#": a += 1
                if lines[i + j][1] == "#": b += 1
                if lines[i + j][2] == "#": c += 1
                if lines[i + j][3] == "#": d += 1
                if lines[i + j][4] == "#": e += 1
            tumblr.append((a, b, c, d, e))
        i += 8
    return keys, tumblr

def main():
    keys, tumblers = parse_input()
    matchCount = 0
    for p0, p1, p2, p3, p4 in tumblers:
        for k0, k1, k2, k3, k4 in keys:
            if p0 + k0 > 5 or p1 + k1 > 5 or p2 + k2 > 5 or p3 + k3 > 5 or p4 + k4 > 5:
                continue
            matchCount += 1
    print(matchCount)


if __name__ == "__main__":
    main()
