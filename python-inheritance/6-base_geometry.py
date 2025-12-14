#!/usr/bin/python3
"""Module 6-base_geometry.py"""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
