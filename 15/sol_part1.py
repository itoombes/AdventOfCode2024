# itoombes, Advent of Code 2024
# Day 15

# Files
INPUT = ("input1.txt", "input2.txt")
DUMMY = ("dummyinput1.txt", "dummyinput2.txt")
TEST_IN = ("testinput1.txt", "testinput2.txt")
# Warehouse chars
WALL_CHAR = "#"
ROBOT_CHAR = "@"
BOX_CHAR = "O"
# Move chars
U_CHAR = "^"
D_CHAR = "v"
L_CHAR = "<"
R_CHAR = ">"
# Move values
U = 0
D = 1
L = 2
R = 3

class Warehouse():
    def __init__(self, files):
        wFileContent = Warehouse.parse_warehouse_file(files[0])
        self._height = wFileContent[0]
        self._width = wFileContent[1]
        self._walls = wFileContent[2]
        self._boxes = wFileContent[3]
        self._robot = wFileContent[4]
        
    def parse_warehouse_file(file):
        f = open(file, "r")
        lines = f.readlines()

        # Parse the file
        height = len(lines)
        width = len(lines[0]) - 1
        walls = list()
        boxes = list()
        origin = None
        # Go through and extract warehouse layout
        for r in range(0, height):
            for w in range(0, width):
                if lines[r][w] == WALL_CHAR:
                    walls.append((r, w))
                elif lines[r][w] == BOX_CHAR:
                    boxes.append((r, w))
                elif lines[r][w] == ROBOT_CHAR:
                    origin = (r, w)
        return (height, width, walls, boxes, origin)

    def parse_instruct_file(file):
        pass

    def __str__(self):
        # Generate representation as array
        array = ["." * self._width] * self._height
        for r, w in self._walls:
            array[r] = array[r][:w] + WALL_CHAR + array[r][w + 1:]
        for r, w in self._boxes:
            array[r] = array[r][:w] + BOX_CHAR + array[r][w + 1:]
        r, w = self._robot
        array[r] = array[r][:w] + ROBOT_CHAR + array[r][w + 1:]
        # Return array as a single string
        string = ""
        for line in array:
            string += line + "\n"
        return string
    

def main():
    warehouse = Warehouse(TEST_IN)
    print(str(warehouse))

if __name__ == "__main__":
    main()
