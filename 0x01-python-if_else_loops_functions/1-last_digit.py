#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 > 5:
    print("Last digit of {} is ".format(number), end="")
    print("{} and is greater than 5".format(number % 10))
elif number % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, number % 10))
elif number % 10 < 6:
    if number < 0:
        number *= -1
        print("Last digit of -{} is ".format(number), end='')
        print("-{} and is less than 6 and not 0".format(number % 10))
    else:
        print("Last digit of {} is ".format(number), end='')
        print("{} and is less than 6 and not 0".format(number % 10))
