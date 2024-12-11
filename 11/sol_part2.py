# itoombes, Advent of Code 2024
# Day 11

import functools

N_ITERATIONS = 25 

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
        return [1]
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone) //2]), int(stone[len(stone) // 2:])]
    return [stone * 2024]

def count_result(depth, stone):
    count = 0
    for i in range(depth, N_ITERATIONS):
        result = apply_rules(stone)
        if len(result) == 1:
            stone = result[0]
            continue
        count += count_result(i, result[0])
        count += count_result(i, result[1])
        return count
    return 1

def main():
    stones = parse_input()
    count = 0
    for stone in stones:
        print(stone)
        count += count_result(0, stone)
    print(len(stones))


if __name__ == "__main__":
    main()
