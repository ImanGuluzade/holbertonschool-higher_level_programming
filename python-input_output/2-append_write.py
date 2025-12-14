#!/usr/bin/python3
"""Function that appends a string to a UTF-8 text file and returns number of characters added"""

def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
