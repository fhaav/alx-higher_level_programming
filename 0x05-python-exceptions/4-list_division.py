#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
        my_list_1: The first list.
        my_list_2: The second list.
        list_length (int): The length of the resulting list.

    Returns:
        A new list (length = list_length) with all divisions.
    """
    new_list = []
    for n in range(list_length):
        try:
            result = 0
            if n < len(my_list_1) and n < len(my_list_2):
                result = my_list_1[n] / my_list_2[n]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return (new_list)
