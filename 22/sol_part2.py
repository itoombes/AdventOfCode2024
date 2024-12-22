# itoombes, Advent of Code 2024
# Day 22

PRUNE = 16777216
N_SECRETS = 10

DUMMY = 1
if DUMMY:
    INPUT = "test.txt"
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

def extract_sequence(value):
    sequence = [value % 10,]
    value = get_next(value)
    deltas = [None,]
    for i in range(1, N_SECRETS):
        sequence.append(value % 10)
        value = get_next(value)
        deltas.append(sequence[i] - sequence[i - 1])
    return sequence, deltas

def main():
    result = 0
    numbers = get_initial_numbers()
    numbers = [123,]
    for number in numbers:
        sequence, deltas = extract_sequence(number)
        print(sequence)
        print(deltas)
    print(result)

if __name__ == "__main__":
    main()
