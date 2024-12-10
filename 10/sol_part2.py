# itoombes, Advent of Code 2024
# Day 10

TESTING = False 

if TESTING:
    INPUT = "dummyinput.txt"
else:
    INPUT = "input.txt"

def parse_map(file):
    f = open(file, "r")
    trailheads = list()
    island = list()
    for r, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        island.append(line)
        if '0' in line:
            for c in range(0, len(line)):
                if line[c] == '0':
                    trailheads.append((r, c))
    return island, trailheads

def score_trailhead(island, trailhead):
    tr, tc = trailhead
    print(f"Scoring trailhead ({tr}, {tc}): ", end="")
    if island[tr][tc] != '0':
        print("Error! Not trailhead")
        return 0

    score = travel_trail(island, -1, tr, tc)
    print(score)

    return score 

def travel_trail(island, prevValue, row, column):
    value = int(island[row][column])
    # Ensure part of trail
    if prevValue + 1 != value:
        return 0
    # Terminate at end of trail
    if value == 9:
        return 1
    # Go thru adjacent paths
    score = 0
    for r, c in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
        if r >= 0 and r < len(island) and c >= 0 and c < len(island[0]):
            score += travel_trail(island, value, r, c)
    return score
            

def main():
    island, trailheads = parse_map(INPUT)
    score = 0
    for trailhead in trailheads:
        score += score_trailhead(island, trailhead)
    print(f"Score is {score}")
    

if __name__ == "__main__":
    main()
