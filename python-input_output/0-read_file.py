#!/usr/bin/python3
"""Function that reads a UTF-8 text file and prints its content"""

def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
