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
        if c == "X":
            # Count the number of 'XMAS'-es
            # Horizontal
            if (ci - 3 >= 0) and (row[ci - 3:ci] == "SAM"):
                count += 1
            if (ci + 3 < col_count) and (row[ci + 1:ci + 4] == "MAS"):
                count += 1
            # Upper
            if ri - 3 >= 0:
                # Upper back diag
                if (ci - 3 >= 0) and (rows[ri - 3][ci - 3] == "S") and (rows[ri - 2][ci - 2] == "A") and (rows[ri - 1][ci - 1] == "M"):
                    count += 1
                # Upper forwards diag
                if (ci + 3 < col_count) and (rows[ri - 3][ci + 3] == "S") and (rows[ri - 2][ci + 2] == "A") and (rows[ri - 1][ci + 1] == "M"):
                    count += 1
                # Upper vertical
                if (rows[ri - 3][ci] == "S") and (rows[ri - 2][ci] == "A") and (rows[ri - 1][ci] == "M"):
                    count += 1
            # Lower 
            if ri + 3 < row_count:
                # Lower back diag
                if (ci - 3 >= 0) and (rows[ri + 3][ci - 3] == "S") and (rows[ri + 2][ci - 2] == "A") and (rows[ri + 1][ci - 1] == "M"):
                    count += 1
                # Lower forwards diag
                if (ci + 3 < col_count) and (rows[ri + 3][ci + 3] == "S") and (rows[ri + 2][ci + 2] == "A") and (rows[ri + 1][ci + 1] == "M"):
                    count += 1
                # Lower vertical
                if (rows[ri + 3][ci] == "S") and (rows[ri + 2][ci] == "A") and (rows[ri + 1][ci] == "M"):
                    count += 1

print(count)
