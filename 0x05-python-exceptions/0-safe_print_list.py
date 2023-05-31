#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Returns:
    The real number of elements printed.
    """
    try:
        num_elem = 0
        for n in range(x):
            print(my_list[n], end="")
            num_elem += 1
        print()
        return num_elem
    except IndexError:
        print()
        return (num_elem)
