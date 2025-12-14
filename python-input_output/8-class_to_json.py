#!/usr/bin/python3
""" Function that returns the dictionary description for JSON serialization """

def class_to_json(obj):
    """
    Returns a dictionary containing all attributes of obj that are serializable.
    """
    return obj.__dict__
