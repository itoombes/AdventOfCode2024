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
        # Parse the warehouse
        wFileContent = Warehouse.parse_warehouse_file(files[0])
        # Number of rows and number of columns
        self._height = wFileContent[0]
        self._width = wFileContent[1]
        # Array in form [(<wall row>, <wall column>),]
        self._walls = wFileContent[2]
        # Array in form [(<box row>, <box column>),]
        self._boxes = wFileContent[3]
        # Robot location as (<row>, <column>)
        self._robot = wFileContent[4]

        # Parse the instructions
        self._cmds = Warehouse.parse_instruction_file(files[1])
        
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

    def parse_instruction_file(file):
        # Read the file as one large string, no newlines
        f = open(file, "r")
        lines = f.readlines()
        cmdString = ""
        for line in lines:
            cmdString += line.replace("\n", "")
        # Convert the string to a char
        cmds = list()
        for c in cmdString:
            if c == U_CHAR: cmds.append(U)
            elif c == D_CHAR: cmds.append(D)
            elif c == L_CHAR: cmds.append(L)
            elif c == R_CHAR: cmds.append(R)

        return cmds

    def get_instruction_string(self):
        string = ""
        for c in self._cmds:
            if c == U: string += U_CHAR
            elif c == D: string += D_CHAR
            elif c == R: string += R_CHAR
            elif c == L: string += L_CHAR
        return string

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
    warehouse = Warehouse(INPUT)
    #warehouse = Warehouse(DUMMY)
    #warehouse = Warehouse(TEST_IN)
    print(str(warehouse))
    print(warehouse.get_instruction_string())

if __name__ == "__main__":
    main()
