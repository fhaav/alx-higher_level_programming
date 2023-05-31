#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value (int): The value to print.

    Returns:
    bool: True if the value is an integer and has been correctly printed,
          False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
