# itoombes, Advent of Code 2024
# Day 4

f = open("input.txt", "r")

# First, convert input into a 2x2 matrix

rows = f.readlines()
row_count = len(rows)
col_count = len(rows[0].replace("\n", ""))

count = 0
for ri, row in enumerate(rows):
    for ci, c in enumerate(row.replace("\n", "")):
        if c == "A" and ri - 1 >= 0 and ri + 1 < row_count and ci - 1 >= 0 and ci + 1 < col_count:
            # Check left to right
            if (rows[ri-1][ci - 1] == "M" and rows[ri+1][ci+1] == "S") or (rows[ri+1][ci + 1] == "M" and rows[ri-1][ci-1] == "S"):    
                # Check right to left
                if (rows[ri-1][ci + 1] == "M" and rows[ri+1][ci-1] == "S") or (rows[ri+1][ci - 1] == "M" and rows[ri-1][ci+1] == "S"):
                    count += 1
print(count)
