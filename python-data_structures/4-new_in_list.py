#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at a specific position without modifying the list."""
    new_list = my_list[:]  # Create a copy of the list
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
