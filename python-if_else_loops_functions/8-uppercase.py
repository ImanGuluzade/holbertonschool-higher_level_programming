#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    out = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # if lowercase letter
            out += "{}".format(chr(ord(c) - 32))
        else:
            out += "{}".format(c)
    print(out)
