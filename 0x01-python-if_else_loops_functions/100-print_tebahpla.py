#!/usr/bin/python3

for i in range(25, -1, -1):
    if (i % 2):
        print(chr(i + ord('a')), end='')
    else:
        print(chr(i + ord('A')), end='')