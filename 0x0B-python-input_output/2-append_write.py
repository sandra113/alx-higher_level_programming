#!/usr/bin/python3
"""This module appends a string to the end of a text file"""


def append_write(filename="", text=""):
    """appends a string to the end of a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
