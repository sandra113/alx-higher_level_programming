#!/usr/bin/python3

import calculator_1

a = 10
b = 5
sum = calculator_1.add(a, b)
dif = calculator_1.sub(a, b)
mult = calculator_1.mul(a, b)
dv = calculator_1.div(a, b)

print("{0} + {1} = {2}".format(a, b, sum))
print("{0} - {1} = {2}".format(a, b, dif))
print("{0} * {1} = {2}".format(a, b, mult))
print("{0} / {1} = {2}".format(a, b, dv))
