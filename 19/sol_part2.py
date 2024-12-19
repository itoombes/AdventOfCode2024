# itoombes, Advent of Code 2024
# Day 19

DUMMY = 0

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
    return pattern_map

def check_possible(design, pattern_map):
    pattern_starts = [0,]
    visited = set()
    while len(pattern_starts) > 0:
        start = pattern_starts.pop(-1)
        visited.add(start)
        if design[start] not in pattern_map.keys():
            continue
        for towel in pattern_map[design[start]]:
            # Ensure not over size
            if start+len(towel) > len(design) + 1:
                continue
            # Ensure a match
            if design[start:start+len(towel)] != towel:
                continue
            # Check if found the end
            if start+len(towel) == len(design):
                return True
            # Add the new start point
            if start+len(towel) not in pattern_starts and start+len(towel) not in visited:
                pattern_starts.append(start+len(towel))

    return False

def count_possible_arrangements(design, pattern_map):
    print(f"Evaluating {design}")
    # Generate a graph connecting every possible pattern
    pattern_starts = [0,]
    edges = {0: set()}
    while len(pattern_starts) > 0:
        start = pattern_starts.pop(0)
        if design[start] not in pattern_map.keys():
            continue
        for towel in pattern_map[design[start]]:
            if start+len(towel) > len(design) + 1:
                continue
            if design[start:start+len(towel)] != towel:
                continue
            if start+len(towel) == len(design):
                edges[start].add("E")
            else:
                edges[start].add(start+len(towel))
                if start+len(towel) not in edges.keys():
                    pattern_starts.append(start+len(towel))
                    edges[start+len(towel)] = set()
    print(edges)
    # Prune the graph
    badEnds = set()
    pruning = True
    while pruning:
        keys = list()
        for k in edges.keys():
            keys.append(k)
        pruning = False
        i = 0
        while i < len(edges.keys()):
            k = keys[i]
            j = 0
            edgeGroup = list()
            for edge in edges[k]:
                edgeGroup.append(edge)
            while j < (len(edges[k])):
                if edgeGroup[j] in badEnds:
                    edges[k].remove(edgeGroup[j])
                    edgeGroup.remove(edgeGroup[j])
                    j = 0
                else: j += 1
            if len(edges[k]) == 0:
                edges.pop(k)
                keys.remove(k)
                badEnds.add(k)
                pruning = True
                i = 0
            else: i += 1
    print(edges)
    
    input()
        

def main():
    patterns, designs = extract_data()
    pattern_map = preprocess_patterns(patterns)
    print(pattern_map)
    possible_designs = list()
    for design in designs:
        if check_possible(design, pattern_map):
            possible_designs.append(design)
    print(possible_designs)
    count = 0
    for design in possible_designs:
        count += count_possible_arrangements(design, pattern_map)
    print(count)

if __name__ == "__main__":
    main()
