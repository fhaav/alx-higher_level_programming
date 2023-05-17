#!/usr/bin/python3
def number_keys(a_dictionary):
    """Return the number of keys in a dictionary."""
    return sum(isinstance(key, (str, int, float, bool))
            for key in a_dictionary)
