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

def compress(data, fileSizes):
    ogData = copy.deepcopy(data)
    iF = 0
    iB = len(data) - 1

    while iF < iB:
        if data[iB] is None:
            data.pop(iB)
            iB -= 1
            continue
        if ogData[iF] is not None:
            iF += 1
            continue
        # Check the amount of free space
        freeIndex = iF
        freeSpace = 0
        while ogData[freeIndex] is None:
            freeSpace += 1
            freeIndex += 1
        # Find the smallest block that fits, starting from the minimum
        copyIndex = iB
        copyLen = 0
        while copyIndex > iF:
            if data[copyIndex] is None or fileSizes[data[copyIndex]] > freeSpace:
                copyIndex -= 1
                continue
            copyLen = fileSizes[data[copyIndex]]
            break
        # If can copy anything, does so
        print(f"Copy to {iF}, copy from {copyIndex}, copy length {copyLen}")
        input("")
        while copyLen > 0:
            data[iF] = data[copyIndex]
            data[copyIndex] = None
            iF += 1
            copyIndex -= 1
            copyLen -= 1
            print_data(data)
        # Move iF to the next block
        while iF < len(data) and ogData[iF] is None:
            iF += 1

    return data

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
    data = compress(data, fileSizes)
    print(checksum(data))

if __name__ == "__main__":
    main()
