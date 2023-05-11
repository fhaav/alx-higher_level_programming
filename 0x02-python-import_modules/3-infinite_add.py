#!/usr/bin/python3

import sys

if __name__ == "__main__":
    def add_arg(argv):
        n = len(argv) - 1
        if n == 0:
            print("{:d}".format(n))
        else:
            total_sum = sum(int(argv[i]) for i in range(1, n+1))
            print("{:d}".format(total_sum))

    add_arg(sys.argv)
