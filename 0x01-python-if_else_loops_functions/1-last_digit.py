#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# L_D = int(str(number)[-1])
L_D = abs(number) % 10
if number < 0:
    L_D = -L_D
    print(f"Last digit of {number} is {L_D}")
elif L_D > 5:
    print(f"Last digit of {number} is {L_D} and is greater than 5")
elif L_D == 0:
    print(f"Last digit of {number} is {L_D} and is 0")
else:
    print(f"Last digit of {number} is {L_D} and is less than 6 and not 0")
