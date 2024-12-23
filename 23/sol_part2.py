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

def check_connectivity(graph, existing_group, vertex):
    for v in existing_group:
        if vertex not in graph[v]:
            return False
    return True

def build_connections(graph):
    vertices = list(graph.keys())
    print(vertices)
    connections = list()
    while len(vertices) > 0:
        subgraph = set()
        frontier = [vertices.pop(0),]
        subgraph.add(frontier[0])
        while len(frontier) > 0:
            v = frontier.pop(0)
            for s in graph[v]:
                if s not in subgraph and check_connectivity(graph, subgraph, s):
                    subgraph.add(s)
                    frontier.append(s)
                    vertices.remove(s)
        print(subgraph)
        connections.append(subgraph)
    return connections
    



def main():
    graph = read_graph()
    subgraphs = build_connections(graph)

if __name__ == "__main__":
    main()
