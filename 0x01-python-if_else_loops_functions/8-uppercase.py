#!/usr/bin/python3
def uppercase(input_str):
    for c in input_str:
        f_s = "{}".format("".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c))
        print(f_s, end='')
    print()
