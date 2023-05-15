#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        length = len(my_list)
        for i in range(length):
            index = length - i - 1
            print("{:d}".format(my_list[index]))
        my_list.reverse()
