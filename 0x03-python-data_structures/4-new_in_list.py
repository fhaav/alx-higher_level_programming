#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    num_elements = len(my_list)
    if num_elements == 0 or idx < 0 or num_elements - 1 < idx:
        return my_list
    for i in range(num_elements):
        new_list.append(my_list[i])
    new_list[idx] = element
    return new_list
