#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
    x (int): The number of elements to access in my_list.
    my_list (list): The list containing elements of any type.

    Returns:
    The real number of integers printed.
    """
    num_elem = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list=[n]), end="")
            num_elem += 1
        except (ValueError, TypeError):
            continue
    print()
    return (num_elem)
