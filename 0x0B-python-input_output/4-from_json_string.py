#!/usr/bin/python3
"""Returns a Python object from a JSON string"""
import json


def from_json_string(my_str):
    """Returns a Python object from a JSON string"""
    return json.loads(my_str)
