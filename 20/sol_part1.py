# itoombes, Advent of Code
# Day 20

import copy

DUMMY = 1
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"

class Track():
    def __init__(self):
        self._track, self._start, self._end = Track.parse_track()
        print(self.return_shortest_path())

    def parse_track():
        track = list()
        for r, line in enumerate(open(INPUT, "r").readlines()):
            track.append(line.replace("\n", ""))
            if "S" in line:
                for c in range(0, len(line)):
                    if line[c] == "S":
                        start = (r, c)
            if "E" in line:
                for c in range(0, len(line)):
                    if line[c] == "E":
                        end = (r, c)
        return (track, start, end)

    def return_shortest_path(self):
        frontier = [(set(), self._start),]
        visited = set()
        visited.add(self._start)
        while len(frontier) > 0:
            path, node = frontier.pop(0)
            r, c = node
            if self._track[r][c] == "E":
                return path
            for sR, sC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                nPath = copy.deepcopy(path)
                nPath.add((sR, sC))
                # Avoid collisions
                if self._track[sR][sC] == "#":
                    continue
                # Add successors to next
                if (sR, sC) not in visited:
                    visited.add((sR, sC))
                    frontier.append((nPath, (sR, sC)))
        return None


def main():
    track = Track()

if __name__ == "__main__":
    main()
