# itoombes, Advent of Code 2024
# Day 22

PRUNE = 16777216

DUMMY = 0
if DUMMY:
    INPUT = "dummy.txt"
else:
    INPUT = "input.txt"

def get_initial_numbers():
    f = open(INPUT, "r")
    numbers = list()
    for line in f.readlines():
        numbers.append(int(line))
    return numbers

def get_next(secret):
    secret = ((secret * 64) ^ secret) % PRUNE
    secret = ((secret // 32) ^ secret) % PRUNE
    secret = ((secret * 2048) ^ secret) % PRUNE
    return secret

def main():
    result = 0
    numbers = get_initial_numbers()
    print(numbers)
    for number in numbers:
        init = number
        for i in range(0, 2000):
            number = get_next(number)
        print(f"{init} : {number}")
        result += number 
    print(result)

if __name__ == "__main__":
    main()
