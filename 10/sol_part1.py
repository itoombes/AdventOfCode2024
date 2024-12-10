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

    # Perform a DFS along the path
    score = 0
    frontier = list()
    visited = list()
    frontier.append((-1, (tr, tc)))
    while len(frontier) != 0:
        # Extract info about location to evaluate
        prevValue, coords = frontier.pop()
        r, c = coords
        value = int(island[r][c])
        # Ensure that it's a valid point in the path
        if prevValue + 1 != value:
            continue
        # If end of path, exit
        if value == 9 and (r, c) not in visited:
            visited.append((r, c))
            score += 1
            continue
        # If here, means you are along the path
        # Add to search
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if nr >= 0 and nr < len(island) and nc >= 0 and nc < len(island[0]):
                frontier.append((value, (nr, nc)))
    
    print(score)

    return score 

def main():
    island, trailheads = parse_map(INPUT)
    score = 0
    for trailhead in trailheads:
        score += score_trailhead(island, trailhead)
    print(f"Score is {score}")
    

if __name__ == "__main__":
    main()
