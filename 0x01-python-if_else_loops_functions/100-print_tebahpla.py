#!/usr/bin/python3

val = ""

for i in range(97, 123):
    val += chr(i)
    val_len = len(val)

for j in range(val_len):
    if j % 2 == 1:
        if 'a' <= val[j] <= 'z':
            upper = ord(val[j]) - ord('a') + ord('A')
            val = val[:j] + chr(upper) + val[j+1:]
print("{}".format(val), end='')
