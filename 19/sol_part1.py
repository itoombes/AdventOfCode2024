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
    pattern_map = dict()
    for pattern in patterns:
        if pattern[0] not in pattern_map:
            pattern_map[pattern[0]] = list()
        pattern_map[pattern[0]].append(pattern)
    return pattern_map

def check_possible(design, pattern_map):
    candidates = list()
    # Add the first candidates
    if design[0] not in pattern_map.keys():
        print(f"No match! {design}")
        return False
    for towel in pattern_map[design[0]]:
        candidates.append(towel)
    
    while len(candidates) > 0:
        currentCandidate = candidates.pop(0)
        if len(currentCandidate) > len(design):
            continue
        if currentCandidate == design:
            print(f"Match! {design} : {currentCandidate}")
            return True
        if currentCandidate == design[0:len(currentCandidate)]:
            if design[len(currentCandidate)] in pattern_map.keys():
                for nextTowel in pattern_map[design[len(currentCandidate)]]:
                    candidates.append(currentCandidate + nextTowel)
    print(f"No match! {design}")
    return False

def main():
    patterns, designs = extract_data()
    pattern_map = preprocess_patterns(patterns)
    count = 0
    for design in designs:
        if check_possible(design, pattern_map):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
