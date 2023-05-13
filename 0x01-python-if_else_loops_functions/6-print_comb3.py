#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while j < 10:
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j), end="")
        else:
            print("{:d}{:d}, ".format(i, j), end="")
        j += 1
    print()
