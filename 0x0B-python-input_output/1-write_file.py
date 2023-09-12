#!/usr/bin/python3
"""This module writes a string into a text file"""


def write_file(filename="", text=""):
    """writes a text into a file and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
