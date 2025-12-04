#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of search by replace in a new list"""
    return [replace if x == search else x for x in my_list]
