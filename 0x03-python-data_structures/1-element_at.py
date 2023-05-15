#!/usr/bin/python3
def element_at(my_list, idx):
    num_elements = len(my_list)
    if (num_elements == 0 or
            idx < 0 or
            num_elements - 1 < idx):
        return None

    return my_list[idx]
