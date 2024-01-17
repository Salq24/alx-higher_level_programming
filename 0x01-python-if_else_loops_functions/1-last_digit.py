#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = number % 10
if l > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l))
elif l == 0:
    print("Last digit of {} is {} and is 0".format(number, l))
else:
    print(f"Last digit of {} is {} and is less than 6 and not 0"(number,l))
