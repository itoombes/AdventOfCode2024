# itoombes, Advent of Code 2024
# Day 22

DUMMY = 1
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

def mix_and_prune(a, b):
    return (a ^ b) % 16776216

def get_next(secret):
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret

def main():
    result = 0
    numbers = get_initial_numbers()
    print(numbers)
    for number in numbers:
        value = number
        for i in range(0, 2001):
            value = get_next(value)
        print(f"{number} : {value}")
        result += value 
    print(result)

if __name__ == "__main__":
    main()
