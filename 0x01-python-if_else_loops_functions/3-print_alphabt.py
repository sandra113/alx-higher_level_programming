#!/usr/bin/python3

for val in range(97, 123):
    if chr(val) not in ('e', 'q'):
        print(chr(val), end='')
