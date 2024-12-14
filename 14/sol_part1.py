# itoombes, Advent of Code 2024
# Day 14

DUMMY = "dummyinput.txt"
INPUT = "input.txt"

WIDTH = 101
HEIGHT = 103
SECONDS = 100

class Robot():
    def __init__(self, px, py, vx, vy):
        self._px = int(px)
        self._py = int(py)
        self._vx = int(vx)
        self._vy = int(vy)

    def __str__(self):
        return f"p={self._px},{self._py}, v={self._vx},{self._vy}"

def get_robots(file):
    f = open(file, "r")
    robots = list()
    for line in f.readlines():
        pos, vel = line.split(" ")
        pos = pos[2:].split(",")
        vel = vel[2:-1].split(",")
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))
    return robots

def main():
    robots = get_robots(INPUT)
    for robot in robots:
        print(robot)

if __name__ == "__main__":
    main()
