#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
l = abs(n) % 10
if l > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, l))
elif l == 0:
    print("Last digit of {} is {} and is 0".format(n, l))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, l))
