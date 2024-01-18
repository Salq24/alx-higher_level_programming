#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_arg = len(sys.argv) - 1
    if n_arg == 1:
        print(("{} argument:").format(n_arg))
    elif n_arg == 0:
        print(("{} arguments.").format(n_arg))
    else:
        print(("{} arguments:").format(n_arg))
    for i in range(1, n_arg + 1):
        print("{}: {}".format(i, sys.argv[i]))
