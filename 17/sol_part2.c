// itoombes, Advent of Code
// Day 17 Part 2

#include <stdio.h>

int program[] = {2, 4, 1, 1, 7, 5, 4, 0, 0, 3, 1, 6, 5, 5, 3, 0};

int get_print_value(int a) {
    return (((((a & 7) ^ 1) ^ (a >> ((a & 7) ^ 1))) ^ 6) & 7);
}

int main() {
    int a0 = 0;
    while (1) {
        int i = 0;
        int ai = a0;
        int valid = 1;
        while ((i < 3) && (valid == 1)) {
            if (get_print_value(ai) != program[i]) {
                valid = 0;
                break;
            }
            ai = ai >> 3;
            i++;
        }
        if ((valid == 1) && (get_print_value(ai) == program[i]) && (ai >> 3 == 0)) {
            break;
        }
        a0++;
    }

    printf("Found! %d", a0);

    while (a0 != 0) {
        printf("%d,", get_print_value(a0));
        a0 = a0 >> 3;
    }

    return 0;
}
