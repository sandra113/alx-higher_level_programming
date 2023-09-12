#!/usr/bin/python3
"""writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
