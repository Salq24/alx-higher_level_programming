#!/usr/bin/python3
for i in range(9):
    for x in range(i + 1, 10):
        print("{:d}{:d}".format(i, x), end=', 'if (i, x) != (8, 9) else '\n')
