# itoombes, Advent of Code 2024
# Day 9

import copy

INPUT = "input.txt"

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
    return (data, block - 1)

def compress(inputData, noFiles):
    data = copy.deepcopy(inputData)
    f = noFiles
 
    # For each file above 0
    while f >= 0:
        print(f"File {f}...")
        # Find the start of the file block
        iB = 0
        while data[iB] != f:
            iB += 1
        # Determine the size of the block
        iS = iB
        fileSize = 0
        while iS < len(data) and data[iS] == f:
            fileSize += 1
            iS += 1
        # Find the next free block on the LHS
        iF = -1
        iS = 0
        freeSize = 0
        while iS < iB:
            if data[iS] is not None:
                freeSize = 0
            else:
                freeSize += 1
            if freeSize == fileSize:
                iF = iS - freeSize + 1
                break
            iS += 1
        # Copy the data
        if iF > -1:
            while fileSize > 0:
                data[iF] = data[iB]
                data[iB] = None
                iF += 1
                iB += 1
                fileSize -= 1
        #print_data(data)
        #input()

        f -= 1

    return data

def checksum(data):
    chksum = 0
    for i, d in enumerate(data):
        if d is not None:
            chksum += d * i
    return chksum

def main():
    diskmap = open_dm(INPUT)
    initData, noFiles = parse_to_array(diskmap)
    print_data(initData)
    compData = compress(initData, noFiles)
    print(checksum(compData))

if __name__ == "__main__":
    main()
