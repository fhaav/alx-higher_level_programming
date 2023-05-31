#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Prints an integer.

    Args:
        value (int): The value to be printed.

    Returns:
        bool: True if value has been correctly printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return (False)
