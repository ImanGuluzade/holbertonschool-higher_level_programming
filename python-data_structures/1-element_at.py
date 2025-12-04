#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list at a specific index.
       Returns None if index is out of range or negative.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
