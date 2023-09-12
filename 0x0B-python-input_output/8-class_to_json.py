#!/usr/bin/python3
"""Returns the dictionary description with simple data structures"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""

    if hasattr(obj, "__dict__"):
        serializable_dict = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_dict[key] = value
        return serializable_dict
    else:
        raise TypeError("Input object is not serializable")
