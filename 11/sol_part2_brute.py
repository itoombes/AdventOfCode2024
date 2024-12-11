# itoombes, Advent of Code 2024
# Day 11

DUMMY = "dummyinput.txt"
INPUT = "input.txt"
N_ITERATIONS = 75 

def parse_input(file):
    f = open(file, "r")
    strings = f.read().split(" ")
    values = list()
    for string in strings:
        values.append(int(string))
    return values

def apply_rules(stones):
    i = 0
    while i < len(stones):
        # Apply rule 1 - if stone is 0
        if stones[i] == 0:
            stones[i] = 1
            i += 1
            continue
        # Apply rule 2 - if stone has even no. of digits
        strStone = str(stones[i])
        digitCount = len(strStone)
        if digitCount % 2 == 0:
            lStone = int(strStone[0:digitCount // 2])
            rStone = int(strStone[(digitCount // 2):])
            leftStones = stones[:i]
            rightStones = stones[i + 1:]
            stones = leftStones + [lStone, rStone] + rightStones
            i += 2
            continue
        # Apply rule 3
        stones[i] = stones[i] * 2024
        i += 1
    return stones

def main():
    stones = parse_input(INPUT)
    print(stones)
    for i in range(0, N_ITERATIONS):
        print(f"Iteration {i + 1}...")
        stones = apply_rules(stones)
        #print(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
