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
    while f > 0:
        print(f"File {f}...")
        # Set back pointer to the end of the correct file
        iB = len(data) - 1
        while iB > 0 and data[iB] != f:
            iB -= 1

        # Now, find the amount of space required by the file
        sizeIndex = iB
        size = 0
        while sizeIndex > 0 and data[sizeIndex] == f:
            sizeIndex -= 1
            size += 1
        # Now, find the starting index of the correct amount of free space, if exists
        freeSpace = 0
        iF = 0
        while iF < sizeIndex:
            if data[iF] is None:
                freeSpace += 1
            else:
                freeSpace = 0
            if freeSpace == size:
                break
            iF += 1
        #print(f"f: {f}; iF : {iF}; iB : {iB}; size : {size}, space : {freeSpace}")
        while freeSpace > 0:
            data[iF] = data[iB]
            data[iB] = None
            iF -= 1
            iB -= 1
            freeSpace -= 1
            #print_data(data)
        #input()
        # go onto the next file
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
    #print_data(initData)
    compData = compress(initData, noFiles)
    print(checksum(compData))

if __name__ == "__main__":
    main()
