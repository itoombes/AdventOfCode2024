# itoombes, Advent of Code 2024
# Day 23

import copy

DUMMY = 1
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

        

def main():
    graph = read_graph()
    groups = extract_groups(graph, 3)
    for i in ("aq","co","de","kh","qp", "tb", "tc", "td", "ub"):
        for v in groups[i]:
            print(f"{i},{v[0]},{v[1]}")

if __name__ == "__main__":
    main()
