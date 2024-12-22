# itoombes, Advent of Code 2024
# Day 22

PRUNE = 16777216
N_SECRETS = 10

DUMMY = 0
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

def extract_patterns(number):
    sequence, deltas = extract_sequence(number)
    pattern = deltas[1:5]
    value = sequence[4]
    pattern_map = {tuple(pattern) : value}
    for i in range(5, len(deltas)):
        # Get the next item in sequence
        pattern.pop(0)
        pattern.append(deltas[i])
        # Detect loop - exit early
        if tuple(pattern) in pattern_map.keys():
            return pattern_map
        pattern_map[tuple(pattern)] = sequence[i]
    return pattern_map

def main():
    result = 0
    numbers = get_initial_numbers()
    numbers = [123,]
    for number in numbers:
        print(extract_patterns(number))
    print(result)

if __name__ == "__main__":
    main()
