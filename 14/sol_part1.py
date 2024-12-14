# itoombes, Advent of Code 2024
# Day 14

DUMMY = "dummyinput.txt"
EDUMMY = "dummydummy.txt"
INPUT = "input.txt"

WIDTH = 101
MIDX = WIDTH // 2
HEIGHT = 103
MIDY = HEIGHT // 2
SECONDS = 100

class Robot():
    def __init__(self, px, py, vx, vy):
        self._px = int(px)
        self._py = int(py)
        self._vx = int(vx)
        self._vy = int(vy) # Moves towards top

    def get_init_position(self):
        return (self._px, self._py)

    def get_final_position(self):
        x = (self._px + self._vx * SECONDS) % WIDTH
        y = (self._py + self._vy * SECONDS) % HEIGHT
        return (x, y)

    def get_quadrant(self):
        x, y = self.get_final_position()
        # Parse quandrant
        if x == MIDX or y == MIDY:
            return None
        if x < MIDX:
            if y < MIDY:
                return "ll"
            else:
                return "ul"
        else:
            if y < MIDY:
                return "lr"
            else:
                return "ur"

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

def print_robots(robots, final):
    environment = list()
    for i in range(0, HEIGHT):
        environment.append("." * WIDTH)
    for robot in robots:
        if final:
            x, y = robot.get_final_position()
        else:
            x, y = robot.get_init_position()
        if environment[y][x] == '.':
            environment[y] = environment[y][:x] + '1' + environment[y][x + 1:]
        else:
            count = int(environment[y][x]) + 1
            environment[y] = environment[y][:x] + str(count) + environment[y][x + 1:]
    for line in environment:
        print(line)
    print() # Newline

def main():
    robots = get_robots(INPUT)
    # Get robots, ensure in correct positions
    for robot in robots:
        print(robot)
    print_robots(robots, False)
    print_robots(robots, True)

    # Establish quadrants
    ul, ur, ll, lr = (0, 0, 0, 0)
    for robot in robots:
        quadrant = robot.get_quadrant()
        if quadrant is None:
            pass
        elif quadrant == "ul":
            ul += 1
        elif quadrant == "ur":
            ur += 1
        elif quadrant == "ll":
            ll += 1
        elif quadrant == "lr":
            lr += 1
    sf = ul * ur * ll * lr
    print(f"Safety factor : {sf}")
     

if __name__ == "__main__":
    main()
