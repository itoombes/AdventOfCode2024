# itoombes, Advent of Code 2024
# Day 17

#PROGRAM = (2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3, 0)
PROGRAM = (2, 4)
# 24
# 11
# 75
# 40
# 03
# 16
# 55
# 30

a0 = 0
while True:
    print(a0)
    ai = a0
    valid = True
    for i in range(0, len(PROGRAM) - 1):
        if (((((ai & 7) ^ 1) ^ (ai // (2 ** ((ai & 7) ^ 1)))) ^ 6) & 7) == PROGRAM[i]:
            ai = ai // 8
        else:
            valid = False
            break
    if valid:
        if (((((ai & 7) ^ 1) ^ (ai // (2 ** ((ai & 7) ^ 1)))) ^ 6) & 7) == PROGRAM[i]:
            if ai // 8 == 0:
                print(f"FOUND! {a0}")
                break
    a0 += 1


for i in range(0, len[PROGRAM]):
    print(((((a0 & 7) ^ 1) ^ (ai // (2 ** ((a0 & 7) ^ 1)))) ^ 6) & 7)
    a0 = a0 // 8
print(a0)
