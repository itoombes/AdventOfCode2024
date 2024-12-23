# itoombes, Advent of Code 2024
# Day 23

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

def main():
    graph = read_graph()
    print(graph)

if __name__ == "__main__":
    main()
