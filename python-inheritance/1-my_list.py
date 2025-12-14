#!/usr/bin/python3
"""Module 1-my_list.py"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
