#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -abs(last)
else:
    last = last
sen = "Last digit of {} is {} and is".format(number, last)
if last > 5:
    print("{} greater than 5".format(sen))
elif last == 0:
    print("{} 0".format(sen))
else:
    print("{} less than 6 and not 0".format(sen))
