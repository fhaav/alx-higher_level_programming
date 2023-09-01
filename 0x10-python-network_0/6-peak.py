#!/usr/bin/python3
"""Implements a peak-finding algorithm."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    Args:
    list_of_integers (list): The list of integers to search for a peak.
    Returns:
    int: Peak value found, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
