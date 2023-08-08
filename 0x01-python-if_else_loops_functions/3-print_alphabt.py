#!/usr/bin/python3

str = ''.join(chr(val) for val in range(97,123) if chr(val) not in ('e', 'q'))
print(str, end='')
