# itoombes, Advent of Code 2024
# Day 19

DUMMY = 1

if DUMMY:
    PATTERNS = "dummy1.txt"
    DESIGNS = "dummy2.txt"
else:
    PATTERNS = "input1.txt"
    DESIGNS = "input2.txt"

def extract_data():
    patterns = list()
    for pattern in open(PATTERNS, "r").readline().split(", "):
        patterns.append(pattern.replace("\n", ""))
    designs = list()
    for line in open(DESIGNS, "r").readlines():
        designs.append(line.replace("\n", ""))
    return patterns, designs

def preprocess_patterns(patterns):
    alphabet = set()
    pattern_map = dict()
    for pattern in patterns:
        if pattern[0] not in pattern_map:
            pattern_map[pattern[0]] = list()
        pattern_map[pattern[0]].append(pattern)
        for c in pattern:
            alphabet.add(c)
    return alphabet, pattern_map

def check_possible(design, alphabet, pattern_map):
    print(f"Evaluating {design}...")
    for c in design:
        if c not in alphabet:
            print(f"\tAlphabet mismatch.")
            return False
    candidates = list()
    # Add the first candidates
    if design[0] not in pattern_map.keys():
        print(f"\tInvalid start!")
        return False
    for towel in pattern_map[design[0]]:
        candidates.append(towel)
    if len(candidates) == 0:
        print(f"\tInvalid start!")
    candidates.sort() # Want largest first
    
    while len(candidates) > 0:
        print(f"\t{candidates}")
        c = candidates.pop(-1) # DFS
        # Check if no more patterns possbile
        if design[len(c)] not in pattern_map:
            continue
        # Evaluate next possible designs
        nextCandidates = list()
        for towel in pattern_map[design[len(c)]]:
            nC = c + towel
            nextCandidates.append(c + towel)
        while len(nextCandidates) > 0:
            nC = min(nextCandidates)
            nextCandidates.remove(nC)
            # See if any of the next patterns short enough
            if len(nC) > len(design):
                continue
            # Ensure a valid match
            if nC == design[:len(nC)]:
                candidates.append(nC)
                if nC == design:
                    print(f"\tMatch! {nC}")
                    return True
    print(f"\tNo match.")
    return False

def main():
    patterns, designs = extract_data()
    alphabet, pattern_map = preprocess_patterns(patterns)
    print(alphabet, pattern_map)
    count = 0
    for design in designs:
        if check_possible(design, alphabet, pattern_map):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
