#!/usr/bin/python3
import sys
def arg_add(args):
    result = sum(int(a) for a in args )
    print(result)
if __name__ == "__main__":
    arg_add(sys.argv[1:])
