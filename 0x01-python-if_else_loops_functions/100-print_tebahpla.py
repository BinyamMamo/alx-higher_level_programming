#!/usr/bin/python3

for i in range(25, -1, -1):
    print("{}".format(chr(i + (ord('a') if (i % 2) else ord('A')))), end='')
