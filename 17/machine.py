# itoombes, Advent of Code 2024
# Day 17

from sys import argv

def main():
    a = int(argv[1]) 
    out = list()
    while a > 0:
        out.append(((((a & 7) ^ 1) ^ (a >> (((a & 7) ^ 1))) ^ 6) & 7))
        a = a >> 3
    print(out)

if __name__ == "__main__":
    main()
