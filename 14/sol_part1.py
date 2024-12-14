# itoombes, Advent of Code 2024
# Day 14

DUMMY = "dummyinput.txt"
INPUT = "input.txt"

WIDTH = 11
MIDX = WIDTH // 2
HEIGHT = 7
MIDY = HEIGHT // 2
SECONDS = 100

class Robot():
    def __init__(self, px, py, vx, vy):
        self._px = int(px)
        self._py = int(py)
        self._vx = int(vx)
        self._vy = int(vy)

    def perform_iterations(self):
        self._px = (self._px + (self._vx * SECONDS)) % WIDTH
        self._py = (self._py + (self._vx * SECONDS)) % HEIGHT 
    
    def get_position(self):
        return (self._px, self._py)

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

def print_robots(robots):
    environment = list()
    for i in range(0, HEIGHT):
        environment.append("." * WIDTH)
    for robot in robots:
        x, y = robot.get_position()
        if environment[y][x] == '.':
            environment[y] = environment[y][:x] + '1' + environment[y][x + 1:]
        else:
            count = int(environment[y][x]) + 1
            environment[y] = environment[y][:x] + str(count) + environment[y][x + 1:]
    for line in environment:
        print(line)

def main():
    robots = get_robots(DUMMY)
    print_robots(robots)


if __name__ == "__main__":
    main()
