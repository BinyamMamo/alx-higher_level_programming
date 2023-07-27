#!/usr/bin/python3

for i in range(25, -1, -1):
    print(chr(i + ord('a')) if (i % 2) else chr(i + ord('A')), end='')
