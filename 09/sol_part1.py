# itoombes, Advent of Code 2024
# Day 9

INPUT = "dummyinput.txt"

def open_dm(file):
    f = open(file)
    content = f.read().replace("\n", "")
    return content

def parse_to_array(diskmap):
    data = list()
    block = 0
    for i in range(0, len(diskmap)):
        if i % 2 == 0:
            for i in range(0, int(diskmap[i])):
                data.append(block)
            block += 1
        else:
            for i in range(0, int(diskmap[i])):
                data.append(None)
    return data

def print_data(data):
    string = ""
    for c in data:
        if c is not None:
            string += str(c)
        else:
            string += ('.')
    print(string)

def main():
    diskmap = open_dm(INPUT)
    initData = parse_to_array(diskmap)
    print_data(initData)

if __name__ == "__main__":
    main()
