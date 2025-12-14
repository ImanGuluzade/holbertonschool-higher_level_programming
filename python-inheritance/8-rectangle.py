#!/usr/bin/python3
"""Module 8-rectangle.py"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize width and height as private attributes after validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Optional: String representation for debugging"""
        return f"<Rectangle width={self.__width} height={self.__height}>"
