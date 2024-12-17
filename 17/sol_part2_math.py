# itoombes, Advent of Code 2024
# Day 17

PROGRAM = (2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3, 0)
# 24
# 11
# 75
# 40
# 03
# 16
# 55
# 30


def perform_iteration(a):
    """
    Returns the output and the next A
    """
    b = (a & 7) ^ 1
    c = a // (2 ** b)
    b = ((b ^ c) ^ 6) & 7
    a = a // 8
    return (a, b)

a = 30899381
while True:
    a, o = perform_iteration(a)
    print(o)
    if a == 0:
        print("Halt")
        break
