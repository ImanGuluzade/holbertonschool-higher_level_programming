#!/usr/bin/python3
"""4-main.py
Test script for 4-rectangle.py
Demonstrates str(), repr(), and eval() recreation.
"""

Rectangle = __import__('4-rectangle').Rectangle

# Create original rectangle
my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# Create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

# Verify new instance is separate but same type
print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
