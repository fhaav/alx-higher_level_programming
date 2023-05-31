#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: The function to be executed.
        *args: Variable number of arguments.

    Returns:
        Any: The result of the function, None otherwise.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return (None)
