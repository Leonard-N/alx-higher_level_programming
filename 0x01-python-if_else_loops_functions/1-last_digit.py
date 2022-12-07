#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L_D = int(str(number)[-1])
if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, L_D))
elif number < 6 =! 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, L_D))
else:
    print("Last digit of {} is {} and is 0".format(number, L_D))
