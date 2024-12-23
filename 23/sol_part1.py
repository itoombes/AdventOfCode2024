# itoombes, Advent of Code 2024
# Day 23

import copy

DUMMY = 0
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"


def read_graph():
    f = open(INPUT, "r")
    graph = dict()
    for line in f.readlines():
        line = line.replace("\n", "")
        a, b = line.split("-")
        if a not in graph.keys():
            graph[a] = set()
        if b not in graph.keys():
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def extract_groups(graph, groupsize):
    groups = dict()
    #graph = copy.deepcopy(graph)
    for v in graph:
        groups[v] = set()
        for secondVertex in graph[v]:
            for thirdVertex in graph[secondVertex]:
                if thirdVertex == v:
                    continue
                if v in graph[thirdVertex]:
                    if thirdVertex < secondVertex:
                        nextGroup = (thirdVertex, secondVertex)
                    else:
                        nextGroup = (secondVertex, thirdVertex)
                    if nextGroup not in groups[v]:
                        groups[v].add(nextGroup)
    return groups

def filter_groups(toFilter):
    groups = set()
    for node in toFilter:
        start, otherGroups = node
        for two, three in otherGroups:
            nextGroup = [start, two, three]
            nextGroup.sort()
            nextGroup = tuple(nextGroup)
            if nextGroup not in groups:
                groups.add(nextGroup)
    return groups

def main():
    graph = read_graph()
    groups = extract_groups(graph, 3)
    validify = list()
    for v in graph.keys():
        if v[0] == "t":
            validify.append((v, groups[v]))
    valid_groups = filter_groups(validify)
    print(valid_groups)
    print(len(valid_groups))

if __name__ == "__main__":
    main()
