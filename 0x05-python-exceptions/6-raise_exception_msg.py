#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raises a name exception with a message.

    Args:
        message (str): The message included in the exception

    Raises:
        NameError: Raises a NameError (always).
    """
    raise NameError(message)
