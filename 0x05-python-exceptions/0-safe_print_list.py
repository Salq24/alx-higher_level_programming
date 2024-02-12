#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cnt = 0
        for a in range(x):
            print(my_list[a], end="")
            cnt += 1
    except IndexError:
        pass
    finally:
        print()
        return cnt
