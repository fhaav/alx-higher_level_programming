#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_d = abs(number) % 10
if number < 0:
    last_d = -last_d

if last_d > 5:
    str_result = "and is greater than 5"
elif last_d == 0:
    str_result = "and is 0"
else:
    str_result = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_d} {str_result}")
