#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L_D = int(str(number)[-1])
# L_D = abs(number) % 10
if L_D > 5:
    print(f"Last digit of {number} is {L_D} and is greater than 5")
elif L_D == 0:
    print(f"Last digit of {number} is {L_D} and is 0")
elif L_D < 6 or L_D != 0:
    print(f"Last digit of {number} is {L_D} and is less than 6 and not 0")
else:
    print("wrong type")
