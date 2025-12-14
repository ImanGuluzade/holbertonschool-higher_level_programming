#!/usr/bin/python3
"""
12-main
Test Pascal's triangle function.
"""

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle in a readable format
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Example: Pascal's triangle with 5 rows
    triangle = pascal_triangle(5)
    print_triangle(triangle)
