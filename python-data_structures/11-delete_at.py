#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list (list): List of elements
        idx (int): Index of element to delete

    Returns:
        list: Updated list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
