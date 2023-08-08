#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number in range(1, 11):
    print(number, end=" is positive")
elif number == 0:
    print(number, end=" is zero")
else:
    print(number, end=" is negative")
