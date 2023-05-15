#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num_elements = len(my_list)
    if (num_elements == 0 or
            idx < 0 or
            num_elements - 1 < idx):
        return my_list

    my_list[idx] = element
    return my_list
