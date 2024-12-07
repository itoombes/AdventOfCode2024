ops = [0] * 3
i = 0
while True:
    if ops[i] == 0:
        ops[i] = 1
        for j in range(0, i):
            ops[j] = 0
    i += 1
    if i == 3:
        break
    else:
        print(ops)
