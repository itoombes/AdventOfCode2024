# itoombes, Advent of Code 2024
# Day 14

import time
from sys import argv

INPUT = "input.txt"

WIDTH = 101
HEIGHT = 103

class Robot():
    def __init__(self, px, py, vx, vy):
        self._px = int(px)
        self._py = int(py)
        self._vx = int(vx)
        self._vy = int(vy) # Moves towards top

    def get_position(self, seconds):
        x = (self._px + self._vx * seconds) % WIDTH
        y = (self._py + self._vy * seconds) % HEIGHT
        return (x, y)

    def __str__(self):
        return f"p={self._px},{self._py}, v={self._vx},{self._vy}"

def get_robots(file):
    f = open(file, "r")
    robots = list()
    for line in f.readlines():
        pos, vel = line.split(" ")
        pos = pos[2:].split(",")
        vel = vel[2:].split(",")
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))
    return robots

def print_robots(robots, seconds):
    print(f"Seconds past: {seconds}")
    environment = list()
    for i in range(0, HEIGHT):
        environment.append(" " * WIDTH)
    for robot in robots:
        x, y = robot.get_position(seconds)
        environment[y] = environment[y][:x] + '#' + environment[y][x + 1:]
    for line in environment:
        print(line)
    print() # Newline

def main():
    if len(argv) != 3:
        print("Use in format \"py sol_part2.py <start> <end>\"")
    i = int(argv[1])
    end = int(argv[2])

    robots = get_robots(INPUT)
    while i < end:
        print_robots(robots, i)
        i += 1
        time.sleep(0.08) # Don't overflow the console

if __name__ == "__main__":
    main()
