#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index.
       Returns the original list if index is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
