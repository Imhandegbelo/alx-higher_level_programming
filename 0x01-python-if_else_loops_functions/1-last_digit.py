#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of " + str(number) + " is ", end="")
remainder = abs(number) % 10
if number < 0:
    remainder = -remainder
if remainder == 0:
    print(str(remainder) + " and is 0")
elif remainder > 5:
    print(str(remainder) + " and is greater than 5")
else:
    print(str(remainder) + " and is less than 6 and not 0")
