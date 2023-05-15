#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        list_length = len(my_list)
        if idx >= 0 and idx < list_length:
            for i in range(list_length):
                if i == idx:
                    my_list.remove(my_list[idx])
                    break
        return my_list
    else:
        return my_list
