#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line"""
     print("{}.format("".join(chr(ord(c)-32) if 'a'<=c <='z' else c for in str)))
