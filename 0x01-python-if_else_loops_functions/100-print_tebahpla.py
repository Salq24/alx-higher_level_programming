#!/usr/bin/python3
for i in range(122, 96, -1):
    x = i % 2
    print("{}".format(chr(i).upper() if x == 1 else chr(i).lower()), end='')
