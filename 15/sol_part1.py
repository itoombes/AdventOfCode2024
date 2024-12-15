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

    def step(self):
        # Perform next step in instructions
        cmd = self._cmds.pop(0)
        if cmd == U:
            self.move_up()
        elif cmd == D:
            self.move_down()
        elif cmd == L:
            self.move_left()
        elif cmd == R:
            self.move_right()

    def attempt_move(self, row, col):
        # Returns True if move collides with box
        # Returns False otherwise
        # If robot changes spot, updates
        if (row, col) in self._walls:
            return False
        if (row, col) not in self._boxes:
            self._robot = (row, col)
            return False
        return True
        # Don't need to check if in bounds - walls enclose the area

    def move_up(self):
        r, c = self._robot
        r -= 1
        if not self.attempt_move(r, c): return
        # Handle box motion
        # Get next free space, if it exists
        rFree = r
        while True:
            rFree -= 1
            if (rFree, c) in self._walls:
                return
            if (rFree, c) not in self._boxes:
                break
        # Update robot and box position
        self._robot = (r, c)
        self._boxes.remove((r, c))
        self._boxes.append((rFree, c))


    def move_down(self):
        r, c = self._robot
        r += 1
        if not self.attempt_move(r, c): return
        # Handle box motion
        rFree = r
        while True:
            rFree += 1
            if (rFree, c) in self._walls:
                return
            if (rFree, c) not in self._boxes:
                break
        self._robot = (r, c)
        self._boxes.remove((r, c))
        self._boxes.append((rFree, c))

    def move_left(self):
        r, c = self._robot
        c -= 1
        if not self.attempt_move(r, c): return
        # Handle box motion
        cFree = c
        while True:
            cFree -= 1
            if (r, cFree) in self._walls:
                return
            if (r, cFree) not in self._boxes:
                break
        self._robot = (r, c)
        self._boxes.remove((r, c))
        self._boxes.append((r, cFree))

    def move_right(self):
        r, c = self._robot
        c += 1
        if not self.attempt_move(r, c): return
        # Handle box motion
        cFree = c
        while True:
            cFree += 1
            if (r, cFree) in self._walls:
                return
            if (r, cFree) not in self._boxes:
                break
        self._robot = (r, c)
        self._boxes.remove((r, c))
        self._boxes.append((r, cFree))



    

def main():
    #warehouse = Warehouse(INPUT)
    #warehouse = Warehouse(DUMMY)
    warehouse = Warehouse(TEST_IN)
    print(str(warehouse))
    print(warehouse.get_instruction_string())
    while True:
        warehouse.step()
        print(str(warehouse))
        input()
if __name__ == "__main__":
    main()
