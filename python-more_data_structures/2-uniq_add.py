#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_numbers = set(my_list)  # Remove duplicates
    total = 0
    for num in unique_numbers:
        total += num
    return total
