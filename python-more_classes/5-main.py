#!/usr/bin/python3
"""5-main.py
Test script for 5-rectangle.py
Demonstrates area, perimeter, str(), repr(), and deletion message.
"""

Rectangle = __import__('5-rectangle').Rectangle

# Create a rectangle
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                        my_rectangle.perimeter()))
print(str(my_rectangle))
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# Delete the rectangle instance
del my_rectangle

# Try to access the deleted object
try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
