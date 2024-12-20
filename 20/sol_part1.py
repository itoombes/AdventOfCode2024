# itoombes, Advent of Code
# Day 20

import copy

DUMMY = 0
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"

class Track():
    def __init__(self):
        self._track, self._start, self._end = Track.parse_track()
        self._times_to_end = self.get_times_to_end()

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

    def get_times_to_end(self):
        times = {self._start : 0}
        visited = set()
        visited.add(self._start)
        cost = 0
        cRow, cCol = self._start
        while True:
            times[(cRow, cCol)] = cost
            cost += 1
            # Have reached the end of the track
            if self._track[cRow][cCol] == "E":
                return times
            # Continue along track
            for sR, sC in ((cRow + 1, cCol), (cRow - 1, cCol), (cRow, cCol + 1), (cRow, cCol - 1)):
                if self._track[sR][sC] == "#" or (sR, sC) in visited:
                    continue
                visited.add((sR, sC))
                cRow = sR
                cCol = sC
                break

    def find_shortcuts(self):
        shortcuts = dict()
        # For every position on the actual track
        for startNode in self._times_to_end.keys():
            startTime = self._times_to_end[startNode]
            startR, startC = startNode
            # Determine available shortcuts 
            successors = list()
            if self._track[startR + 1][startC] == "#":
                successors.append((startR + 2, startC))
            if self._track[startR - 1][startC] == "#":
                successors.append((startR - 2, startC))
            if self._track[startR][startC + 1] == "#":
                successors.append((startR, startC + 2))
            if self._track[startR][startC - 1] == "#":
                successors.append((startR, startC - 2))
            # Process potential shortcuts
            for s in successors:
                # Make sure part of the track
                if s not in self._times_to_end:
                    continue
                # Process shortcut
                timeSaved = self._times_to_end[s] - startTime - 2
                if timeSaved > 0:
                    if timeSaved not in shortcuts:
                        shortcuts[timeSaved] = 1
                    else:
                        shortcuts[timeSaved] += 1

        return shortcuts

def main():
    track = Track()
    shortcuts = track.find_shortcuts()
    cheats = 0
    for time in shortcuts.keys():
        if time >= 100:
            cheats += shortcuts[time]
    print(cheats)

if __name__ == "__main__":
    main()
