#!/usr/bin/env python3
"""
Convert CSV file to JSON file
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and save to data.json

    Args:
        csv_filename (str): CSV file to read from

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data_list = list(reader)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except (FileNotFoundError, csv.Error, json.JSONDecodeError, OSError):
        return False
