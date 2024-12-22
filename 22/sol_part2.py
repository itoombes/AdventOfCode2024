# itoombes, Advent of Code 2024
# Day 22

PRUNE = 16777216
# Number of secrets, including initial
N_SECRETS = 2000

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
    # First item in sequence
    sequence = [value % 10,]
    value = get_next(value)
    deltas = [None,]
    for i in range(1, N_SECRETS):
        sequence.append(value % 10)
        value = get_next(value)
        deltas.append(sequence[i] - sequence[i - 1])
    #print(sequence)
    #print(deltas)
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
    numbers = get_initial_numbers()
    #numbers = [123,]
    patterns = dict()
    for number in numbers:
        print(f"Processing {number}...")
        new_patterns = extract_patterns(number)
        for k in new_patterns.keys():
            if k in patterns.keys():
                patterns[k].append(new_patterns[k])
            else:
                patterns[k] = [new_patterns[k],]
    print(patterns)
    maximum = 0
    for v in patterns.values():
        instance = 0
        for num in v:
            instance += num
        if instance > maximum: maximum = instance

    print(maximum)


    print(result)

if __name__ == "__main__":
    main()
