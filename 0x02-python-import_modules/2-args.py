#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args) - 1

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, args[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, args[i]))
