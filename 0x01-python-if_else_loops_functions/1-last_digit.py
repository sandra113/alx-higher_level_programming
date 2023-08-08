#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(abs(number))
num_length = len(number_str)
i = number_str[num_length - 1]
i = int(i)
if i == 0:
    print("Last digit of", number, "is", i, "and is 0")
elif i > 5:
    print("Last digit of", number, "is", i, "and is greater than 5")
elif i < 6:
    print("Last digit of", number, "is", i, "and is less than 6 and not 0")
