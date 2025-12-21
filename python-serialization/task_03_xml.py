#!/usr/bin/env python3
"""
XML serialization and deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to a file.

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): XML filename to save
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except OSError:
        return False
    return True


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): XML filename to read

    Returns:
        dict: Deserialized Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except (ET.ParseError, FileNotFoundError, OSError):
        return None
