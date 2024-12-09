# itoombes, Advent of Code 2024
# Day 9

import copy

INPUT = "dummyinput.txt"

def print_data(data):
    string = ""
    for c in data:
        if c is not None:
            string += str(c)
        else:
            string += ('.')
    print(string)

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

def compress(inputData):
    data = copy.deepcopy(inputData)

    iF = 0
    iB = len(data) - 1

    while iF < iB:
        # Ensure iF and iB are at valid locations
        if data[iF] is not None:
            iF += 1
            continue
        if data[iB] is None:
            data.pop(iB)
            iB -= 1
            continue
                
        # Front pointer at free space
        # Back pointer at not free
        # Copy across
        data[iF] = data.pop(iB)
        iB -= 1
        print_data(data)

    return data

def main():
    diskmap = open_dm(INPUT)
    initData = parse_to_array(diskmap)
    print_data(initData)
    compData = compress(initData)

if __name__ == "__main__":
    main()
