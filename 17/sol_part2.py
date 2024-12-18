# itoombes, Advent of Code
# Day 17 Part 2 Attempt 3

#program = [2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3, 0]
program = [2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3]

# Last 'a' value must be 7
currentValid = [7,]
# a = 0b00000000[a2,a1,a0]
# Then, build upwards
i = len(program) - 1
while i > 0:
    nextValid = list()
    for a in currentValid:
        a << 3
        for least_sig_bits in range(0, 8):
            ai = a + least_sig_bits
            out = (((least_sig_bits ^ 1) ^ (ai >> ((least_sig_bits ^ 1))) ^ 6) & 7)
            if out == program[i]:
                nextValid.append(ai)
    currentValid = nextValid
    print(currentValid)
    input()
    i -= 1

print(currentValid)

# Can go backwards over this 
# Know that >> 3 at end of every 3, so build up A backwards

