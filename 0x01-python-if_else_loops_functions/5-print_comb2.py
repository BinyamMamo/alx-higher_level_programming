#!/usr/bin/python3

for x in range(0, 100):
    print(f"{x:02d}", end="")
    if x == 99:
        break
    print(", ", end="")
