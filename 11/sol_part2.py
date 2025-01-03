# itoombes, Advent of Code 2024
# Day 11

import functools

N_ITERATIONS = 75

def parse_input():
    f = open("input.txt", "r")
    strings = f.read().split(" ")
    values = list()
    for string in strings:
        values.append(int(string))
    return values

@functools.cache
def apply_rules(stone):
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        lStone = int(str(stone)[:len(str(stone)) // 2])
        rStone = int(str(stone)[len(str(stone)) // 2:])
        #print(f"\tSplit : {stone} -> {lStone}, {rStone}")
        return [lStone, rStone]
    return stone * 2024

@functools.cache
def count_result(depth, stone):
    while depth < N_ITERATIONS:
        #print(f"\tDepth: {depth}; Stone: {stone}")
        stone = apply_rules(stone)
        depth += 1
        if type(stone) is list:
            #print("\tEvaluate split!")
            return count_result(depth, stone[0]) + count_result(depth, stone[1])
    return 1

def main():
    stones = parse_input()
    count = 0
    for stone in stones:
        print(stone)
        res = count_result(0, stone)
        print(f"\t{res}")
        count += res
        print(f"\t{count}")
    print(count)


if __name__ == "__main__":
    main()
