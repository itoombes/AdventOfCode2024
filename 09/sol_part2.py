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

def parse_diskmap(diskmap):
    data = list()
    fileNo = 0
    fileSizes = dict()
    for i in range(0, len(diskmap)):
        if i % 2 == 0:
            fileSize = 0
            for i in range(0, int(diskmap[i])):
                data.append(fileNo)
                fileSize += 1
            fileSizes[fileNo] = fileSize 
            fileNo += 1
        else:
            for i in range(0, int(diskmap[i])):
                data.append(None)
    return (data, fileSizes)

def compress(inputData):
    data = copy.deepcopy(inputData)
    pass

def checksum(data):
    chksum = 0
    for i, d in enumerate(data):
        if d is not None:
            chksum += d * i
    return chksum

def main():
    diskmap = open_dm(INPUT)
    data, fileSizes = parse_diskmap(diskmap)
    print_data(data)
    print(fileSizes)

if __name__ == "__main__":
    main()
