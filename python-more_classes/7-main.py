#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

# Create first rectangle
my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")

# Change instance print_symbol
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

# Create second rectangle
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")

# Change class print_symbol, affects new instances
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

# Create third rectangle
my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)
print("--")

# Change third rectangle print_symbol to a list
my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)
print("--")

# Delete all rectangles
del my_rectangle_1
del my_rectangle_2
del my_rectangle_3
